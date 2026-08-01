import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

class KeyA():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color, x_offset=0):
        image = pygame.Surface((width, height))  
        image.fill(color)
        image.blit(self.sheet, (0, 0), (x_offset + frame * width, 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image

def RenderKeyA():
    key_a = pygame.image.load(resource_path("data/A_spritesheet.png")).convert_alpha()
    Spritesheet = KeyA(key_a)
    frames = 5
    width, height = 32, 32
    x_offset = 0
    scale = 4.0
    colorkey = (10, 10, 10)

    animation_list = []
    for i in range(frames):
        animation_list.append(Spritesheet.get_image(i, width, height, scale, colorkey, x_offset))

    return animation_list

class KeyS():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color, x_offset=0):
        image = pygame.Surface((width, height))  
        image.fill(color)
        image.blit(self.sheet, (0, 0), (x_offset + frame * width, 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image

def RenderKeyS():
    key_s = pygame.image.load(resource_path("data/S_spritesheet.png")).convert_alpha()
    Spritesheet = KeyS(key_s)
    frames = 5
    width, height = 32, 32
    x_offset = 0
    scale = 4.0
    colorkey = (10, 10, 10)

    animation_list = []
    for i in range(frames):
        animation_list.append(Spritesheet.get_image(i, width, height, scale, colorkey, x_offset))

    return animation_list

class KeyD():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color, x_offset=0):
        image = pygame.Surface((width, height))  
        image.fill(color)
        image.blit(self.sheet, (0, 0), (x_offset + frame * width, 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image

def RenderKeyD():
    key_d = pygame.image.load(resource_path("data/D_spritesheet.png")).convert_alpha()
    Spritesheet = KeyD(key_d)
    frames = 5
    width, height = 32, 32
    x_offset = 0
    scale = 4.0
    colorkey = (10, 10, 10)

    animation_list = []
    for i in range(frames):
        animation_list.append(Spritesheet.get_image(i, width, height, scale, colorkey, x_offset))

    return animation_list

class KeyW():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color, x_offset=0):
        image = pygame.Surface((width, height))  
        image.fill(color)
        image.blit(self.sheet, (0, 0), (x_offset + frame * width, 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image

def RenderKeyW():
    key_w = pygame.image.load(resource_path("data/W_spritesheet.png")).convert_alpha()
    Spritesheet = KeyW(key_w)
    frames = 5
    width, height = 32, 32
    x_offset = 0
    scale = 4.0
    colorkey = (10, 10, 10)

    animation_list = []
    for i in range(frames):
        animation_list.append(Spritesheet.get_image(i, width, height, scale, colorkey, x_offset))

    return animation_list

# [Key Render Functions]
def LoadKeyA(screen, frame, pos):
    screen.blit(frame, pos)
def LoadKeyS(screen, frame, pos):
    screen.blit(frame, pos)
def LoadKeyD(screen, frame, pos):
    screen.blit(frame, pos)
def LoadKeyW(screen, frame, pos):
    screen.blit(frame, pos)