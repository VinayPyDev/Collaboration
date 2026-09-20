import json
import os
import sys
import pygame
from font import get_font

pygame.init()


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)


def load_tmj(filepath, tile_images):
    with open(filepath, "r") as f:
        tmj_data = json.load(f)

    tile_width = tmj_data["tilewidth"]
    tile_height = tmj_data["tileheight"]

    parsed_tiles = []
    hitboxes = []

    def parse_layers(layers_list):
        for layer in layers_list:
            if layer.get("type") == "group":
                parse_layers(layer.get("layers", []))

            elif layer.get("type") == "tilelayer":
                data = layer.get("data", [])
                width_in_tiles = layer.get("width", 0)

                for index, gid in enumerate(data):
                    if gid == 0:
                        continue

                    col = index % width_in_tiles
                    row = index // width_in_tiles
                    x = col * tile_width
                    y = row * tile_height

                    image = tile_images.get(gid)
                    if image:
                        parsed_tiles.append(
                            {
                                "image": image,
                                "pos": (x, y),
                                "gid": gid,
                                "rect": pygame.Rect(
                                    x, y, tile_width, tile_height
                                ),
                            }
                        )

            elif layer.get("type") == "objectgroup":
                for obj in layer.get("objects", []):
                    hitbox_rect = pygame.Rect(
                        int(obj["x"]),
                        int(obj["y"]),
                        int(obj.get("width", tile_width)),
                        int(obj.get("height", tile_height)),
                    )
                    properties = {
                        prop["name"]: prop["value"]
                        for prop in obj.get("properties", [])
                    }

                    hitboxes.append(
                        {
                            "name": obj.get("name", ""),
                            "type": obj.get("type", ""),
                            "gid": obj.get("gid"),
                            "rect": hitbox_rect,
                            "properties": properties,
                        }
                    )

    parse_layers(tmj_data.get("layers", []))
    return parsed_tiles, hitboxes


def game1(screen):
    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()

    images = {
        1: pygame.image.load(resource_path("data2/bottle.png")).convert_alpha(),
        2: pygame.image.load(resource_path("data2/bowl.png")).convert_alpha(),
        3: pygame.image.load(resource_path("data2/foodbag.png")).convert_alpha(),
        4: pygame.image.load(resource_path("data2/trashbag.png")).convert_alpha(),
        5: pygame.image.load(resource_path("data2/trashbin.png")).convert_alpha(),
        6: pygame.image.load(resource_path("data2/wall.png")).convert_alpha(),
        7: pygame.image.load(resource_path("data2/wall2.png")).convert_alpha(),
    }

    tiles, map_objects = load_tmj("map.tmj", images)

    pickup_items = []
    dog_rect = pygame.Rect(800, 500, 100, 100)

    for obj in map_objects:
        if obj["type"] == "food":
            pickup_items.append(
                {"rect": obj["rect"], "gid": 3, "type": "food"}
            )
        elif obj["type"] == "water":
            pickup_items.append(
                {"rect": obj["rect"], "gid": 1, "type": "water"}
            )
        elif obj["type"] == "dog":
            dog_rect = obj["rect"]

    wall_gids = {6, 7}
    wall_rects = [tile["rect"] for tile in tiles if tile["gid"] in wall_gids]

    player_rect = pygame.Rect(640, 360, 100, 100)
    player_pos_x = float(player_rect.x)
    player_pos_y = float(player_rect.y)
    speed = 500

    food_scored = 0
    water_scored = 0
    water_needs = 2
    food_needs = 3

    while True:
        dt = clock.tick(60) / 1000
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode(
                    (WIDTH, HEIGHT), pygame.RESIZABLE
                )
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and water_scored > 0:
                    water_scored -= 1
                    water_needs = max(0, water_needs - 1)
                elif event.key == pygame.K_e and food_scored > 0:
                    food_scored -= 1
                    food_needs = max(0, food_needs - 1)

        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0
        if keys[pygame.K_a]:
            dx -= speed * dt
        if keys[pygame.K_d]:
            dx += speed * dt
        if keys[pygame.K_s]:
            dy += speed * dt
        if keys[pygame.K_w]:
            dy -= speed * dt

        player_pos_x += dx
        player_rect.x = round(player_pos_x)
        for wall in wall_rects:
            if player_rect.colliderect(wall):
                if dx > 0:
                    player_rect.right = wall.left
                elif dx < 0:
                    player_rect.left = wall.right
                player_pos_x = float(player_rect.x)

        player_pos_y += dy
        player_rect.y = round(player_pos_y)
        for wall in wall_rects:
            if player_rect.colliderect(wall):
                if dy > 0:
                    player_rect.bottom = wall.top
                elif dy < 0:
                    player_rect.top = wall.bottom
                player_pos_y = float(player_rect.y)

        camera_x = player_rect.x - WIDTH // 2
        camera_y = player_rect.y - HEIGHT // 2

        for tile in tiles:
            tile_x = tile["pos"][0] - camera_x
            tile_y = tile["pos"][1] - camera_y
            screen.blit(tile["image"], (tile_x, tile_y))

        for item in pickup_items[:]:
            item_rect = item["rect"]
            item_image = images.get(item["gid"])

            if item_image:
                screen.blit(
                    item_image,
                    (item_rect.x - camera_x, item_rect.y - camera_y),
                )

            if player_rect.colliderect(item_rect):
                if item["type"] == "food":
                    food_scored += 1
                elif item["type"] == "water":
                    water_scored += 1
                pickup_items.remove(item)

        pygame.draw.rect(
            screen,
            "green",
            (
                dog_rect.x - camera_x,
                dog_rect.y - camera_y,
                dog_rect.width,
                dog_rect.height,
            ),
        )

        if player_rect.colliderect(dog_rect):
            water_dog_needs = get_font(40).render(
                f"E to feed: {food_needs}", True, (255, 255, 255)
            )
            food_dog_needs = get_font(40).render(
                f"F to water: {water_needs}", True, (255, 255, 255)
            )
            screen.blit(water_dog_needs, (700, 400))
            screen.blit(food_dog_needs, (700, 300))

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (
                player_rect.x - camera_x,
                player_rect.y - camera_y,
                player_rect.width,
                player_rect.height,
            ),
        )

        text1 = get_font(50).render(
            f"Food: {food_scored}", True, (255, 255, 255)
        )
        text2 = get_font(50).render(
            f"Water: {water_scored}", True, (255, 255, 255)
        )
        screen.blit(text1, (0, 0))
        screen.blit(text2, (0, 100))

        if food_needs == 0 and water_needs == 0:
            return False

        pygame.display.update()


if __name__ == "__main__":
    main_screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    game1(main_screen)