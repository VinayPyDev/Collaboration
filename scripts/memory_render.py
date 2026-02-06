import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

class Memory_1():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def Render_memory_1():
    memory_1_img = pygame.image.load(resource_path("Memory/memory1_sheet.png")).convert_alpha()
    SpriteSheet = Memory_1(memory_1_img)
    frames = 23
    width, height = 300, 300
    scale = 1.0
    colorkey = (255, 255, 255)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class Memory_2():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def Render_memory_2():
    memory_2_img = pygame.image.load(resource_path("Memory/memory2.png")).convert_alpha()
    SpriteSheet = Memory_2(memory_2_img)
    frames = 20
    width, height = 300, 300
    scale = 1.0
    colorkey = (255, 255, 255)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class Memory_3():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def Render_memory_3():
    memory_3_img = pygame.image.load(resource_path("Memory/memory3.png")).convert_alpha()
    SpriteSheet = Memory_3(memory_3_img)
    frames = 14
    width, height = 300, 300
    scale = 1.0
    colorkey = (255, 255, 255)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class Memory_4():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image    

def Render_memory_4():
    memory_4_img = pygame.image.load(resource_path("Memory/memory4.png")).convert_alpha()
    SpriteSheet = Memory_4(memory_4_img)
    frames = 20
    width, height = 300, 300
    scale = 1.0
    colorkey = (255, 255, 255)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class Memory_5():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image    

def Render_memory_5():
    memory_5_img = pygame.image.load(resource_path("Memory/memory5.png")).convert_alpha()
    SpriteSheet = Memory_5(memory_5_img)
    frames = 44
    width, height = 300, 300
    scale = 1.0
    colorkey = (255, 255, 255)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class Memory_6():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image    

def Render_memory_6():
    memory_6_img = pygame.image.load(resource_path("Memory/memory6.png")).convert_alpha()
    SpriteSheet = Memory_6(memory_6_img)
    frames = 16
    width, height = 300, 300
    scale = 1.0
    colorkey = (255, 255, 255)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list


class Memory_7():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image    

def Render_memory_7():
    memory_7_img = pygame.image.load(resource_path("Memory/memory7.png")).convert_alpha()
    SpriteSheet = Memory_7(memory_7_img)
    frames = 37
    width, height = 300, 300
    scale = 1.0
    colorkey = (255, 255, 255)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list
