import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

# TODO [27-06-26]: Tilesets new import calls
def Load_Sunrise_Tileset():
    sunrise_img1 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile1.png"))
    sunrise_img1.set_colorkey((255, 255, 255))
    sunrise_img2 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile2.png"))
    sunrise_img2.set_colorkey((255, 255, 255))
    sunrise_img3 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile3.png"))
    sunrise_img3.set_colorkey((255, 255, 255))
    sunrise_img4 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile4.png"))
    sunrise_img4.set_colorkey((255, 255, 255))
    sunrise_img5 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile5.png"))
    sunrise_img5.set_colorkey((255, 255, 255))
    sunrise_img6 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile6.png"))
    sunrise_img6.set_colorkey((255, 255, 255))
    sunrise_img7 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile7.png"))
    sunrise_img7.set_colorkey((255, 255, 255))
    sunrise_img8 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile8.png"))
    sunrise_img8.set_colorkey((255, 255, 255))
    sunrise_img9 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile9.png"))
    sunrise_img9.set_colorkey((255, 255, 255))
    sunrise_img10 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile10.png"))
    sunrise_img10.set_colorkey((255, 255, 255))
    sunrise_img11 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile11.png"))
    sunrise_img11.set_colorkey((255, 255, 255))
    sunrise_img12 = pygame.image.load(resource_path("tiles/Sunrise/sunrise_tile12.png"))
    sunrise_img12.set_colorkey((255, 255, 255))
    return {
        "sun_1": sunrise_img1,
        "sun_2": sunrise_img2,
        "sun_3": sunrise_img3,
        "sun_4": sunrise_img4,
        "sun_5": sunrise_img5,
        "sun_6": sunrise_img6,
        "sun_7": sunrise_img7,
        "sun_8": sunrise_img8,
        "sun_9": sunrise_img9,
        "sun_10": sunrise_img10,
        "sun_11": sunrise_img11,
        "sun_12": sunrise_img12
    }

def Load_Dungeon_Tileset():
    dungeon_img1 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile1.png"))
    dungeon_img1.set_colorkey((255, 255, 255))
    dungeon_img2 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile2.png"))
    dungeon_img2.set_colorkey((255, 255, 255))
    dungeon_img3 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile3.png"))
    dungeon_img3.set_colorkey((255, 255, 255))
    dungeon_img4 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile4.png"))
    dungeon_img4.set_colorkey((255, 255, 255))
    dungeon_img5 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile5.png"))
    dungeon_img5.set_colorkey((255, 255, 255))
    dungeon_img6 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile6.png"))
    dungeon_img6.set_colorkey((255, 255, 255))
    dungeon_img7 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile7.png"))
    dungeon_img7.set_colorkey((255, 255, 255))
    dungeon_img8 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile8.png"))
    dungeon_img8.set_colorkey((255, 255, 255))
    dungeon_img9 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile9.png"))
    dungeon_img9.set_colorkey((255, 255, 255))
    dungeon_img10 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile10.png"))
    dungeon_img10.set_colorkey((255, 255, 255))
    dungeon_img11 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile11.png"))
    dungeon_img11.set_colorkey((255, 255, 255))
    dungeon_img12 = pygame.image.load(resource_path("tiles/Dungeon/dungeon_tile12.png"))
    dungeon_img12.set_colorkey((255, 255, 255))
    return {
        "dungeon_1": dungeon_img1,
        "dungeon_2": dungeon_img2,
        "dungeon_3": dungeon_img3,
        "dungeon_4": dungeon_img4,
        "dungeon_5": dungeon_img5,
        "dungeon_6": dungeon_img6,
        "dungeon_7": dungeon_img7,
        "dungeon_8": dungeon_img8,
        "dungeon_9": dungeon_img9,
        "dungeon_10": dungeon_img10,
        "dungeon_11": dungeon_img11,
        "dungeon_12": dungeon_img12
    }

def Load_Void_Tileset():
    void_img1 = pygame.image.load(resource_path("tiles/Void/void_tile1.png"))
    void_img1.set_colorkey((255, 255, 255))
    void_img2 = pygame.image.load(resource_path("tiles/Void/void_tile2.png"))
    void_img2.set_colorkey((255, 255, 255))
    void_img3 = pygame.image.load(resource_path("tiles/Void/void_tile3.png"))
    void_img3.set_colorkey((255, 255, 255))
    void_img4 = pygame.image.load(resource_path("tiles/Void/void_tile4.png"))
    void_img4.set_colorkey((255, 255, 255))
    void_img5 = pygame.image.load(resource_path("tiles/Void/void_tile5.png"))
    void_img5.set_colorkey((255, 255, 255))
    void_img6 = pygame.image.load(resource_path("tiles/Void/void_tile6.png"))
    void_img6.set_colorkey((255, 255, 255))
    void_img7 = pygame.image.load(resource_path("tiles/Void/void_tile7.png"))
    void_img7.set_colorkey((255, 255, 255))
    void_img8 = pygame.image.load(resource_path("tiles/Void/void_tile8.png"))
    void_img8.set_colorkey((255, 255, 255))
    void_img9 = pygame.image.load(resource_path("tiles/Void/void_tile9.png"))
    void_img9.set_colorkey((255, 255, 255))
    void_img10 = pygame.image.load(resource_path("tiles/Void/void_tile10.png")) 
    void_img10.set_colorkey((255, 255, 255))
    void_img11 = pygame.image.load(resource_path("tiles/Void/void_tile11.png")) 
    void_img11.set_colorkey((255, 255, 255))
    void_img12 = pygame.image.load(resource_path("tiles/Void/void_tile12.png")) 
    void_img12.set_colorkey((255, 255, 255))
    void_img13 = pygame.image.load(resource_path("tiles/Void/void_tile13.png")) 
    void_img13.set_colorkey((255, 255, 255))
    void_img14 = pygame.image.load(resource_path("tiles/Void/void_tile14.png")) 
    void_img14.set_colorkey((255, 255, 255))
    return {
        "void_1": void_img1,
        "void_2": void_img2,
        "void_3": void_img3,
        "void_4": void_img4,
        "void_5": void_img5,
        "void_6": void_img6,
        "void_7": void_img7,
        "void_8": void_img8,
        "void_9": void_img9,
        "void_10": void_img10,
        "void_11": void_img11,
        "void_12": void_img12,
        "void_13": void_img13,
        "void_14": void_img14
    }