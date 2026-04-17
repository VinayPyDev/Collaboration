import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

class SunriseTileset():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, rect, scale=1.0, color=(255, 255, 255)):
        x, y, width, height = rect

        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (x, y, width, height))

        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        image.set_colorkey(color)
        return image
    
def Render_Sunrise_Tileset():
    sheet_img = pygame.image.load(resource_path("data/sunrise_tileset.png")).convert_alpha()
    SpriteSheet = SunriseTileset(sheet_img)

    scale = 1.0
    colorkey = (255, 255, 255)

    tile_14 = pygame.image.load(resource_path("data/grass_tileset_dpad.png")).convert_alpha()
    tile_15 = pygame.image.load(resource_path("data/grass_tileset_dpad2.png")).convert_alpha()

    sprites = {
        "tile_1": (0, 0, 48, 48),

        "tile_2": (48, 0, 16, 16),
        "tile_3": (96, 0, 16, 16),
        "tile_4": (48, 48, 16, 16),
        "tile_5": (96, 48, 16, 16), 

        "tile_6": (0, 48, 16, 16),
        "tile_7": (48, 32, 16, 16),

        "tile_9": (0, 80, 16, 16),
        "tile_10": (32, 80, 16, 16),
        "tile_11": (96, 16, 16, 16),
        "tile_12": (96, 32, 16, 16),

        "tile_13": (119, 0, 24, 48),

        "tile_14": tile_14,
        "tile_15": tile_15
    }

    sprite_images = {}

    for name, data in sprites.items():
        if isinstance(data, tuple):
            sprite_images[name] = SpriteSheet.get_image(data, scale, colorkey)
        else:
            sprite_images[name] = data

    return sprite_images

class DungeonTileset():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, rect, scale=1.0, color=(255, 255, 255)):
        x, y, width, height = rect

        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (x, y, width, height))

        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        image.set_colorkey(color)
        return image
    
def Render_Dungeon_Tileset():
    sheet_img = pygame.image.load(resource_path("data/dungeon_tileset.png")).convert_alpha()
    SpriteSheet = DungeonTileset(sheet_img)

    scale = 1.0
    colorkey = (255, 255, 255)

    # dpad like structures that would be added later :D
    tile_12 = pygame.image.load(resource_path("data/dungeon_tileset_dpad.png")).convert_alpha()

    sprites = {
        "tile_1": (0, 0, 48, 48),

        "tile_2": (48, 0, 16, 16),
        "tile_3": (96, 0, 16, 16),
        "tile_4": (48, 48, 16, 16),
        "tile_5": (96, 48, 16, 16),

        "tile_6": (46, 95, 16, 17),
        "tile_7": (68, 99, 6, 6),
        "tile_8": (15, 95, 16, 16),

        "tile_9": (86, 64, 14, 45),
        "tile_10": (48, 0, 47, 46),
        "tile_11": (65, 48, 30, 27),
        "tile_12": tile_12
    }

    sprite_images = {}

    for name, data in sprites.items():
        if isinstance(data, tuple):
            sprite_images[name] = SpriteSheet.get_image(data, scale, colorkey)
        else:
            sprite_images[name] = data

    return sprite_images

class VoidTileset():
     def __init__(self, image):
        self.sheet = image
    
     def get_image(self, rect, scale=1.0, color=(255, 255, 255)):
        x, y, width, height = rect

        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (x, y, width, height))

        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        image.set_colorkey(color)
        return image
    
def Render_Void_Tileset():
    sheet_img = pygame.image.load(resource_path("data/void_tileset.png")).convert_alpha()
    SpriteSheet = VoidTileset(sheet_img)

    scale = 1.0
    colorkey = (0, 0, 0)

    tile_6 = pygame.image.load(resource_path("data/void_tileset2_dpad.png")).convert_alpha()
    tile_13 = pygame.image.load(resource_path("data/void_tileset2_area.png")).convert_alpha()

    sprites = {
        "tile_1": (0, 0, 48, 48),
        "tile_2": (48, 3, 16, 16),
        "tile_3": (96, 0, 16, 16),
        
        "tile_4": (48, 22, 16, 18),
        "tile_5": (96, 22, 16, 18),
        "tile_6": tile_6,

        "tile_7": (0, 48, 16, 16),
        "tile_8": (15, 48, 16, 16),
        "tile_9": (32, 48, 16, 16),
        "tile_10": (48, 48, 16, 16),

        "tile_11": (0, 64, 16, 16),
        "tile_12": (16, 64, 32, 16),
        "tile_13": tile_13,

        "tile_14": (0, 80, 32, 16)
    }

    sprite_images = {}

    for name, data in sprites.items():
        if isinstance(data, tuple):
            sprite_images[name] = SpriteSheet.get_image(data, scale, colorkey)
        else:
            sprite_images[name] = data

    return sprite_images