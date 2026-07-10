import pygame
import sys
import os 

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

class jumpscare_1():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def Render_jumpscare_1():
    jumpscare_img_1 = pygame.image.load(resource_path("jumpscares/2ndJumpscareV2.png")).convert_alpha()
    SpriteSheet = jumpscare_1(jumpscare_img_1)
    frames = 51
    width, height = 150, 150
    scale = 1.0
    colorkey = (255, 255, 255)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class jumpscare_2():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def Render_jumpscare_2():
    jumpscare_img_2 = pygame.image.load(resource_path("jumpscares/LockerJumpscare.png")).convert_alpha()
    SpriteSheet = jumpscare_2(jumpscare_img_2)
    frames = 32
    width, height = 150, 150
    scale = 1.0
    colorkey = (0, 0, 255)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list