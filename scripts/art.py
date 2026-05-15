import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

# Player Idle Animations
class PlayerIdleRight():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color, x_offset=0):
        image = pygame.Surface((width, height))  
        image.fill(color)
        image.blit(self.sheet, (0, 0), (x_offset + frame * width, 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image

def RenderPlayerIdleRight():
    Idle_right_spritesheet = pygame.image.load(resource_path("player_animations/idle/idle_right.png")).convert_alpha()
    Spritesheet = PlayerIdleRight(Idle_right_spritesheet)
    frames = 20
    width, height = 64, 86
    x_offset = 19
    scale = 150 / 64
    colorkey = (10, 10, 10)

    animation_list = []
    for i in range(frames):
        animation_list.append(Spritesheet.get_image(i, width, height, scale, colorkey, x_offset))

    return animation_list

class PlayerIdleLeft():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color, x_offset=0):
        image = pygame.Surface((width, height))  
        image.fill(color)
        image.blit(self.sheet, (0, 0), (x_offset + frame * width, 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image

def RenderPlayerIdleLeft():
    Idle_left_spritesheet = pygame.image.load(resource_path("player_animations/idle/idle_left.png")).convert_alpha()
    Spritesheet = PlayerIdleLeft(Idle_left_spritesheet)
    frames = 20
    width, height = 64, 86
    x_offset = 19
    scale = 150 / 64
    colorkey = (10, 10, 10)

    animation_list = []
    for i in range(frames):
        animation_list.append(Spritesheet.get_image(i, width, height, scale, colorkey, x_offset))

    return animation_list

class PlayerMoveRight():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color, x_offset=0):
        image = pygame.Surface((width, height))  
        image.fill(color)
        image.blit(self.sheet, (0, 0), (x_offset + frame * width, 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image

def RenderPlayerMoveRight():
    Move_right_spritesheet = pygame.image.load(resource_path("player_animations/walk/moving_right.png")).convert_alpha()
    Spritesheet = PlayerMoveRight(Move_right_spritesheet)
    frames = 24
    width, height = 64, 86
    x_offset = 19
    scale = 150 / 64
    colorkey = (10, 10, 10)

    animation_list = []
    for i in range(frames):
        animation_list.append(Spritesheet.get_image(i, width, height, scale, colorkey, x_offset))

    return animation_list

class PlayerMoveLeft():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color, x_offset=0):
        image = pygame.Surface((width, height))  
        image.fill(color)
        image.blit(self.sheet, (0, 0), (x_offset + frame * width, 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image

def RenderPlayerMoveLeft():
    Move_Left_spritesheet = pygame.image.load(resource_path("player_animations/walk/moving_left.png")).convert_alpha()
    Spritesheet = PlayerMoveLeft(Move_Left_spritesheet)
    frames = 24
    width, height = 64, 86
    x_offset = 19
    scale = 150 / 64
    colorkey = (10, 10, 10)

    animation_list = []
    for i in range(frames):
        animation_list.append(Spritesheet.get_image(i, width, height, scale, colorkey, x_offset))

    return animation_list

def load_sunset_bg_full():
    return {
        "sunset": pygame.transform.scale(pygame.image.load(resource_path("data/sunsetbg_full.png")).convert_alpha(), (3000, 720))
    }

def load_sunset_extra():
    return {
        "sunset_ex": pygame.transform.scale(pygame.image.load(resource_path("data/sunset_extra.png")).convert_alpha(), (3000, 720))
    }

def load_sunset_bg_2_full():
    return {
        "sunset_2": pygame.transform.scale(pygame.image.load(resource_path("data/sunset_bg_2.png")).convert_alpha(), (3000, 720))
    }

def load_dungeon_bg_full():
    return {
        "dungeon": pygame.transform.scale(pygame.image.load(resource_path("data/dungeonbg_full.png")).convert_alpha(), (3000, 720))
    }

def load_void_bg_full():
    return {
        "void": pygame.transform.scale(pygame.image.load(resource_path("data/voidbg.png")).convert_alpha(), (3000, 720))
    }

def load_keys():
    return {
        "key1": pygame.image.load(resource_path("data/sprite-0001.png")).convert_alpha(),
        "key2": pygame.image.load(resource_path("data/sprite-0003.png")).convert_alpha(),
        "key3": pygame.image.load(resource_path("data/sprite-0004.png")).convert_alpha(),
        "key4": pygame.image.load(resource_path("data/sprite-0005.png")).convert_alpha()
    }