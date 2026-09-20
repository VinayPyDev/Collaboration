import pygame
import sys
import os
import json

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def get_font(size):
    return pygame.font.Font(resource_path("font/PixeloidSans.ttf"), size)

def get_font_BOLD(size):
    return pygame.font.Font(resource_path("font/PixeloidSans-Bold.ttf"), size)

pygame.init()

tile_size = 32

images = {
    1: pygame.image.load(resource_path("data2/bottle.png")).convert_alpha(),
    2: pygame.image.load(resource_path("data2/bowl.png")).convert_alpha(),
    3: pygame.image.load(resource_path("data2/foodbag.png")).convert_alpha(),
    4: pygame.image.load(resource_path("data2/trashbag.png")).convert_alpha(),
    5: pygame.image.load(resource_path("data2/trashbin.png")).convert_alpha(),
    6: pygame.image.load(resource_path("data2/wall.png")).convert_alpha(),
    7: pygame.image.load(resource_path("data2/wall2.png")).convert_alpha()
}

def LoadTmj(filepath, tile_images, tile_width, tile_height):
    with open(filepath, "r") as f:
        tmj_data = json.load(f)

    parsed_tiles = []
    hitbox = []

    for layer in tmj_data.get("layers", []):
        if layer["type"] == "tilelayer":
            width_tiles = layer["width"]
            data = layer["data"]

            for idx, gid in enumerate(data):
                if gid == 0:
                    continue

                col = idx % width_tiles
                row = idx % width_tiles
                x = col * tile_width
                y = row * tile_height

                img = tile_images.get(gid)
                if img:
                    parsed_tiles.append({
                        "image": img,
                        "pos": (x, y)
                    })
        elif layer["type"] == "objectgroup":
            for obj in layer.get("objects", []):
                hitbox_rect = pygame.Rect(
                    int(obj["x"]),
                    int(obj["y"]),
                    int(obj["width"]),
                    int(obj["height"]),
                )
                properties = {
                    prop["name"]: prop["value"]
                    for prop in obj.get("properties", [])
                }
                hitbox.append({
                    "name": obj.get("name", ""),
                    "type": obj.get("type", ""),
                    "rect": hitbox_rect,
                    "properties": properties
                })

    return parsed_tiles, hitbox

# print("---", __file__)

def game1():
    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()
    dt = 0

    camera_x = 0
    camera_y = 0

    rect = pygame.Rect(640, 360, 100, 100)
    speed = 500

    food_scored = 0
    water_scored = 0

    tiles, map_objs = LoadTmj(
        "map.tmj", images, tile_width=32, tile_height=32
    )

    rect2 = pygame.Rect(100, 300, 64, 64)
    rect3 = pygame.Rect(400, 200, 64, 64)
    rect4 = pygame.Rect(700, 100, 64, 64)
    rect5 = pygame.Rect(500, 500, 64, 64)
    rect6 = pygame.Rect(1100, 600, 64, 64)

    dog_rect = pygame.Rect(800, 500, 100, 100)
    water_needs = 2
    food_needs = 3

    not_picked1 = True
    not_picked2 = True
    not_picked3 = True
    not_picked4 = True
    not_picked5 = True

    while True:
        dt = clock.tick(60) / 1000
        screen.fill("#28396b")

        if not_picked1:
            pygame.draw.rect(screen, "blue", (rect2.x - camera_x, rect2.y - camera_y, rect2.width, rect2.height))
        if not_picked2:
            pygame.draw.rect(screen, "yellow", (rect3.x - camera_x, rect3.y - camera_y, rect3.width, rect3.height))
        if not_picked3:
            pygame.draw.rect(screen, "blue", (rect4.x - camera_x, rect4.y - camera_y, rect4.width, rect4.height))
        if not_picked4:
            pygame.draw.rect(screen, "yellow", (rect5.x - camera_x, rect5.y - camera_y, rect5.width, rect5.height))
        if not_picked5:
            pygame.draw.rect(screen, "blue", (rect6.x - camera_x, rect6.y - camera_y, rect6.width, rect6.height))

        pygame.draw.rect(screen, "green", (dog_rect.x - camera_x, dog_rect.y - camera_y, dog_rect.width, dog_rect.height))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE | pygame.SCALED)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and water_scored > 0:
                    water_scored -= 1
                    water_needs -= 1
                elif event.key == pygame.K_e and food_scored > 0:
                    food_scored -= 1
                    food_needs -= 1

        camera_x = rect.x - WIDTH // 2
        camera_y = rect.y - HEIGHT // 2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            rect.x -= speed * dt
        if keys[pygame.K_d]:
            rect.x += speed * dt
        if keys[pygame.K_s]:
            rect.y += speed * dt
        if keys[pygame.K_w]:
            rect.y -= speed * dt

        if not_picked1 and rect.colliderect(rect2):
            not_picked1 = False
            food_scored = food_scored + 1
        if not_picked2 and rect.colliderect(rect3):
            not_picked2 = False
            water_scored = water_scored + 1
        if not_picked3 and rect.colliderect(rect4):
            not_picked3 = False
            food_scored = food_scored + 1
        if not_picked4 and rect.colliderect(rect5):
            not_picked4 = False
            water_scored = water_scored + 1
        if not_picked5 and rect.colliderect(rect6):
            not_picked5 = False
            food_scored = food_scored + 1        

        water_dog_needs = get_font(40).render(f"E to feed: {food_needs}", True, (255, 255, 255))
        food_dog_needs = get_font(40).render(f"F to water: {water_needs}", True, (255, 255, 255))

        if rect.colliderect(dog_rect):
            screen.blit(water_dog_needs, (700, 400))
            screen.blit(food_dog_needs, (700, 300))

            if food_scored < 0:
                food_scored = 0
            elif water_scored < 0:
                water_scored = 0

            if food_needs < 0:
                food_needs = 0
            if water_needs < 0:
                water_needs = 0

        text1 = get_font(50).render(f"Food: {food_scored}", True, (255, 255, 255))
        text2 = get_font(50).render(f"Water: {water_scored}", True, (255, 255, 255))
        screen.blit(text1, (0, 0))
        screen.blit(text2, (0, 100))

        pygame.draw.rect(screen, (255, 0, 0), (rect.x - camera_x, rect.y - camera_y, rect.width, rect.height))
    
        if food_needs == 0 and water_needs == 0:
            return False

        pygame.display.update()
