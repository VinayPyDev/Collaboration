import json, os, math
import xml.etree.ElementTree as ET
import pygame


# ═══════════════════════════════════════════════════════════════
# TSX PARSER
# ═══════════════════════════════════════════════════════════════

def _parse_tsx(path):
    """Parse a .tsx (XML) tileset into a dict matching the JSON schema."""
    tree = ET.parse(path)
    root = tree.getroot()

    result = {
        "name": root.get("name", ""),
        "tilewidth": int(root.get("tilewidth", 0)),
        "tileheight": int(root.get("tileheight", 0)),
        "columns": int(root.get("columns", 0)),
        "tilecount": int(root.get("tilecount", 0)),
        "spacing": int(root.get("spacing", 0)),
        "margin": int(root.get("margin", 0)),
    }

    img_el = root.find("image")
    if img_el is not None:
        result["image"] = img_el.get("source", "")

    tiles = []
    for tile_el in root.findall("tile"):
        tile_def = {"id": int(tile_el.get("id", 0))}

        og_el = tile_el.find("objectgroup")
        if og_el is not None:
            objects = []
            for obj_el in og_el.findall("object"):
                obj = {}
                for attr in ("x", "y", "width", "height"):
                    val = obj_el.get(attr)
                    if val is not None:
                        obj[attr] = int(float(val))
                if "width" in obj and "height" in obj:
                    objects.append(obj)
            if objects:
                tile_def["objectgroup"] = {"objects": objects}

        tile_img = tile_el.find("image")
        if tile_img is not None:
            tile_def["image"] = tile_img.get("source", "")

        tiles.append(tile_def)

    if tiles:
        result["tiles"] = tiles

    return result


# ═══════════════════════════════════════════════════════════════
# COLLISION EXTRACTOR
# ═══════════════════════════════════════════════════════════════

def _extract_tile_collision(first_gid, tile_def, collisions):
    og = tile_def.get("objectgroup")
    if not og:
        return
    gid = first_gid + tile_def["id"]
    rects = []
    for obj in og.get("objects", []):
        if "width" in obj and "height" in obj:
            rects.append((obj["x"], obj["y"], obj["width"], obj["height"]))
    if rects:
        collisions[gid] = rects


# ═══════════════════════════════════════════════════════════════
# MAIN LOADER
# ═══════════════════════════════════════════════════════════════

def load_infinite_tiled(path):
    """
    Parse a .tmj infinite map.
    Returns (tile_w, tile_h, tile_images, layers, collisions).
    """
    map_dir = os.path.dirname(os.path.abspath(path))

    with open(path, "r") as f:
        raw = json.load(f)

    tile_w = raw["tilewidth"]
    tile_h = raw["tileheight"]
    tile_images = {}
    collisions = {}

    for ts in raw.get("tilesets", []):
        first_gid = ts.get("firstgid", 1)

        # ── Resolve external tileset ────────────────────────────
        if "source" in ts:
            src_path = os.path.join(map_dir, ts["source"])
            if ts["source"].endswith((".json", ".tsj")):
                with open(src_path, "r") as f2:
                    ts_data = json.load(f2)
            else:
                ts_data = _parse_tsx(src_path)
            # Merge: external data takes priority, keep firstgid from map
            ts = {**ts_data, "firstgid": first_gid}
            ts["_ts_dir"] = os.path.dirname(os.path.abspath(src_path))

        # ── Image collection (per-tile PNGs) ────────────────────
        if "image" not in ts and "tiles" in ts:
            for tile_def in ts["tiles"]:
                if "image" not in tile_def:
                    continue
                base = ts.get("_ts_dir", map_dir)
                full = os.path.join(base, tile_def["image"])
                surf = pygame.image.load(full).convert_alpha()
                tile_images[first_gid + tile_def["id"]] = surf
                _extract_tile_collision(first_gid, tile_def, collisions)
            continue

        # ── Single-image tileset (sprite sheet) ─────────────────
        if "image" not in ts:
            continue

        base = ts.get("_ts_dir", map_dir)
        full = os.path.join(base, ts["image"])
        img = pygame.image.load(full).convert_alpha()

        cols = ts.get("columns", 0)
        if cols == 0:
            cols = max(1, math.ceil(math.sqrt(ts.get("tilecount", 1))))
        spacing = ts.get("spacing", 0)
        margin  = ts.get("margin", 0)
        count   = ts.get("tilecount", 0)

        for i in range(count):
            gid = first_gid + i
            sx  = margin + (i % cols) * (tile_w + spacing)
            sy  = margin + (i // cols) * (tile_h + spacing)
            if sx + tile_w <= img.get_width() and sy + tile_h <= img.get_height():
                tile_images[gid] = img.subsurface(sx, sy, tile_w, tile_h)

        for tile_def in ts.get("tiles", []):
            _extract_tile_collision(first_gid, tile_def, collisions)

    # ── Layers & chunks ─────────────────────────────────────────
    layers = []
    for layer in raw.get("layers", []):
        if layer.get("type") != "tilelayer" or not layer.get("visible", True):
            continue
        chunks = [
            (c["x"], c["y"], c["width"], c["height"], c["data"])
            for c in layer.get("chunks", [])
        ]
        if chunks:
            layers.append((layer.get("name", ""), chunks))

    return tile_w, tile_h, tile_images, layers, collisions


# ═══════════════════════════════════════════════════════════════
# MAP
# ═══════════════════════════════════════════════════════════════

class InfiniteMap:
    def __init__(self, path):
        (self.tile_w, self.tile_h,
         self.tile_images, self.layers, self.collisions) = load_infinite_tiled(path)

    def get_tile_at(self, tx, ty):
        for _, chunks in self.layers:
            for cx, cy, cw, ch, data in chunks:
                lx, ly = tx - cx, ty - cy
                if 0 <= lx < cw and 0 <= ly < ch:
                    return data[ly * cw + lx]
        return 0

    def render(self, screen, cam_x, cam_y, sw, sh):
        min_cx = math.floor(cam_x / self.tile_w)
        min_cy = math.floor(cam_y / self.tile_h)
        max_cx = math.ceil((cam_x + sw) / self.tile_w)
        max_cy = math.ceil((cam_y + sh) / self.tile_h)

        for _, chunks in self.layers:
            for cx, cy, cw, ch, data in chunks:
                if cx + cw <= min_cx or cx >= max_cx:
                    continue
                if cy + ch <= min_cy or cy >= max_cy:
                    continue
                for row in range(ch):
                    for col in range(cw):
                        gid = data[row * cw + col]
                        if gid == 0:
                            continue
                        tile = self.tile_images.get(gid)
                        if tile is None:
                            continue
                        screen.blit(tile, (
                            int((cx + col) * self.tile_w - cam_x),
                            int((cy + row) * self.tile_h - cam_y),
                        ))


# ═══════════════════════════════════════════════════════════════
# PLAYER
# ═══════════════════════════════════════════════════════════════

class Player:
    def __init__(self, x, y, w, h, speed=3):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.speed = speed

    def update(self, keys, game_map):
        dx = dy = 0
        if keys[pygame.K_LEFT]:  dx -= self.speed
        if keys[pygame.K_RIGHT]: dx += self.speed
        if keys[pygame.K_UP]:    dy -= self.speed
        if keys[pygame.K_DOWN]:  dy += self.speed

        self.x += dx
        if self._collides(game_map):
            self.x -= dx

        self.y += dy
        if self._collides(game_map):
            self.y -= dy

    def _collides(self, m):
        min_tx = int(self.x // m.tile_w)
        max_tx = int((self.x + self.w - 1) // m.tile_w)
        min_ty = int(self.y // m.tile_h)
        max_ty = int((self.y + self.h - 1) // m.tile_h)

        for ty in range(min_ty, max_ty + 1):
            for tx in range(min_tx, max_tx + 1):
                gid = m.get_tile_at(tx, ty)
                if gid == 0 or gid not in m.collisions:
                    continue
                for cx, cy, cw, ch in m.collisions[gid]:
                    rx = tx * m.tile_w + cx
                    ry = ty * m.tile_h + cy
                    if (self.x < rx + cw and self.x + self.w > rx and
                        self.y < ry + ch and self.y + self.h > ry):
                        return True
        return False

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.w, self.h)


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    game_map = InfiniteMap("map.tmj")
    player = Player(64, 64, 24, 24)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys, game_map)

        cam_x = int(player.x - screen.get_width()  / 2)
        cam_y = int(player.y - screen.get_height() / 2)

        screen.fill((0, 0, 0))
        game_map.render(screen, cam_x, cam_y, screen.get_width(), screen.get_height())
        pygame.draw.rect(screen, (255, 0, 0), player.rect())

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()   