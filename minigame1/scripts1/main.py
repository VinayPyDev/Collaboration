import pygame
import random
import sys
import os
import json
import xml.etree.ElementTree as ET

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

screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE | pygame.SCALED)

tileset = pygame.image.load(
    resource_path("minigame_tileset1.png")
).convert_alpha()
mapx = -1000
mapy = -1000

images = {}

scale = 3
tile_size = 32

for gid in range(1, 8):
    tile = tileset.subsurface(
        ((gid - 1) * tile_size, 0, tile_size, tile_size)
    ).copy()
    images[gid] = pygame.transform.scale(tile, (tile_size*scale, tile_size*scale))

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
        x = col * 96 + mapx
        y = row * 96 + mapy

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

bottle_img = pygame.transform.scale(pygame.image.load(resource_path("data2/bottle.png")).convert_alpha(), (150, 150))
foodbag_img = pygame.transform.scale(pygame.image.load(resource_path("data2/foodbag.png")).convert_alpha(), (150, 150))
bowl_img = pygame.transform.scale(pygame.image.load(resource_path("data2/bowl.png")).convert_alpha(), (150, 150))

def game1():
    global screen
    global tsx, map_tiles, map_data, mapx, mapy
    global collisions, collision, hitboxes, root, images, tileset, gid
    global objectgroup, tile, tile_id, idx, col, row, width

    global bottle_img, foodbag_img, bowl_img

    WIDTH, HEIGHT = screen.get_size()
    clock = pygame.time.Clock()
    dt = 0

    camera_x = 0
    camera_y = 0

    rect = pygame.Rect(640, 360, 100, 100)
    speed = 500

    food_scored = 0
    water_scored = 0

    rect2 = pygame.Rect(random.uniform(600, 500), random.uniform(500, 2176), 96, 96)
    rect3 = pygame.Rect(random.uniform(808, -52), random.uniform(500, 2176), 96, 96)
    rect4 = pygame.Rect(random.uniform(560, 1360), random.uniform(500, 2176), 96, 96)
    rect5 = pygame.Rect(random.uniform(1170, -108), random.uniform(500, 2176), 96, 96)
    rect6 = pygame.Rect(random.uniform(530, -14), random.uniform(500, 2176), 96, 96)

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
        screen.fill("#0c1120")

        if not_picked1:
            screen.blit(foodbag_img, (rect2.x - camera_x, rect2.y - camera_y))
        if not_picked2:
            screen.blit(bottle_img, (rect3.x - camera_x, rect3.y - camera_y))
        if not_picked3:
            screen.blit(foodbag_img, (rect4.x - camera_x, rect4.y - camera_y))
        if not_picked4:
            screen.blit(bottle_img, (rect5.x - camera_x, rect5.y - camera_y))
        if not_picked5:
            screen.blit(foodbag_img, (rect6.x - camera_x, rect6.y - camera_y))

        pygame.draw.rect(screen, "green", (dog_rect.x - camera_x, dog_rect.y - camera_y, dog_rect.width, dog_rect.height))
        screen.blit(bowl_img, (775 - camera_x, 550 - camera_y))

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

        print(int(rect.x))
        print(int(rect.y))

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

        for hitbox in hitboxes:
            if rect.colliderect(hitbox):
                if rect.x > 0:
                    rect.bottom = hitbox.top
                elif rect.y < 0:
                    rect.top = hitbox.bottom

        for tile in map_tiles:
            image = images[tile["gid"]]
            screen.blit(
                image, (tile["x"] - camera_x, tile["y"] - camera_y)   
            )

        text1 = get_font(50).render(f"Food: {food_scored}", True, (255, 255, 255))
        text2 = get_font(50).render(f"Water: {water_scored}", True, (255, 255, 255))
        screen.blit(text1, (0, 0))
        screen.blit(text2, (0, 100))

        pygame.draw.rect(screen, (255, 0, 0), (rect.x - camera_x, rect.y - camera_y, rect.width, rect.height))
    
        if food_needs == 0 and water_needs == 0:
            return False

        pygame.display.update()
# game1()