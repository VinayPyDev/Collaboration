import json
import pygame
import os
import sys
import xml.etree.ElementTree as ET

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

tileset = pygame.image.load(
    resource_path("minigame_tileset1.png")
).convert_alpha()

mapx = -100
mapy = -100

images = {}

for gid in range(1, 8):
    images[gid] = tileset.subsurface(
        ((gid - 1) * 32, 0, 32, 32)
    ).copy()

with open("minigame_tileset1.tsx", "r") as f:
    tsx = f.read()

root = ET.fromstring(tsx)

collisions = {}

for tile in root.findall("tile"):
    tile_id = int(tile.get("id"))
    gid = tile_id + 1

    objectgroup = tile.find("objectgroup")

    if objectgroup is None:
        continue

    collisions[gid] = []

    for obj in objectgroup.findall("object"):
        rect = pygame.Rect(
            float(obj.get("x", 0)),
            float(obj.get("y", 0)),
            float(obj.get("width", 0)),
            float(obj.get("height", 0))
        )

        collisions[gid].append(rect)

with open("map2.tmj", "r") as f:
    map_data = json.load(f)

map_tiles = []
hitboxes = []
for layer in map_data["layers"]:
    if layer["type"] != "tilelayer":
        continue
    width = layer["width"]

    for idx, gid in enumerate(layer["data"]):
        if gid == 0:
            continue

        col = idx % width
        row = idx // width
        x = col * 32 + mapx
        y = row * 32 + mapy

        map_tiles.append({
            "gid": gid,
            "x": x, 
            "y": y
        })

        for collision in collisions.get(gid, []):

            hitboxes.append(
                pygame.Rect(
                    x + collision.x,
                    y + collision.y,
                    collision.width,
                    collision.height
                )
            )

player = pygame.Rect(640, 360, 24, 24)
running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    dx = 0
    dy = 0

    if keys[pygame.K_a]:
        dx -= 200 * dt

    if keys[pygame.K_d]:
        dx += 200 * dt

    if keys[pygame.K_w]:
        dy -= 200 * dt

    if keys[pygame.K_s]:
        dy += 200 * dt

    player.x += dx

    for hitbox in hitboxes:

        if player.colliderect(hitbox):

            if dx > 0:
                player.right = hitbox.left

            elif dx < 0:
                player.left = hitbox.right

    player.y += dy

    for hitbox in hitboxes:

        if player.colliderect(hitbox):

            if dy > 0:
                player.bottom = hitbox.top

            elif dy < 0:
                player.top = hitbox.bottom


    screen.fill((30, 30, 30))

    for tile in map_tiles:

        image = images[tile["gid"]]

        screen.blit(
            image,
            (tile["x"], tile["y"])
        )

    # for hitbox in hitboxes:

    #     pygame.draw.rect(
    #         screen,
    #         (255, 0, 0),
    #         hitbox,
    #         1
    #     )

    pygame.draw.rect(
        screen,
        (0, 255, 0),
        player
    )


    pygame.display.flip()


pygame.quit()