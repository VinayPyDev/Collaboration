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
    return {
        "sun_1": sunrise_img1 := pygame.image.load(resource_path("tiles/sunrise_tile1.png")).convert_alpha(), sunrise_img1.set_colorkey((255, 255, 255))),
        "sun_2": sunrise_img2 := pygame.image.load(resource_path("tiles/sunrise_tile2.png")).convert_alpha(), sunrise_img2.set_colorkey((255, 255, 255))),
        "sun_3": sunrise_img3 := pygame.image.load(resource_path("tiles/sunrise_tile3.png")).convert_alpha(), sunrise_img3.set_colorkey((255, 255, 255))),
        "sun_4": sunrise_img4 := pygame.image.load(resource_path("tiles/sunrise_tile4.png")).convert_alpha(), sunrise_img4.set_colorkey((255, 255, 255))),
        "sun_5": sunrise_img5 := pygame.image.load(resource_path("tiles/sunrise_tile5.png")).convert_alpha(), sunrise_img5.set_colorkey((255, 255, 255))),
        "sun_6": sunrise_img6 := pygame.image.load(resource_path("tiles/sunrise_tile6.png")).convert_alpha(), sunrise_img6.set_colorkey((255, 255, 255))),
        "sun_7": sunrise_img7 := pygame.image.load(resource_path("tiles/sunrise_tile7.png")).convert_alpha(), sunrise_img7.set_colorkey((255, 255, 255))),
        "sun_8": sunrise_img8 := pygame.image.load(resource_path("tiles/sunrise_tile8.png")).convert_alpha(), sunrise_img8.set_colorkey((255, 255, 255))),
        "sun_9": sunrise_img9 := pygame.image.load(resource_path("tiles/sunrise_tile9.png")).convert_alpha(), sunrise_img9.set_colorkey((255, 255, 255))),
        "sun_10": sunrise_img10 := pygame.image.load(resource_path("tiles/sunrise_tile10.png")).convert_alpha(), sunrise_img10.set_colorkey((255, 255, 255))),
        "sun_11": sunrise_img11 := pygame.image.load(resource_path("tiles/sunrise_tile11.png")).convert_alpha(), sunrise_img11.set_colorkey((255, 255, 255))),
        "sun_12": sunrise_img12 := pygame.image.load(resource_path("tiles/sunrise_tile12.png")).convert_alpha(), sunrise_img12.set_colorkey((255, 255, 255)))
    }

def Load_Dungeon_Tileset():
    return {
        "dungeon_1": dungeon_img1 := pygame.image.load(resource_path("tiles/dungeon_tile1.png")).convert_alpha(), dungeon_img1.set_colorkey((255, 255, 255))),
        "dungeon_2": dungeon_img2 := pygame.image.load(resource_path("tiles/dungeon_tile2.png")).convert_alpha(), dungeon_img2.set_colorkey((255, 255, 255))),
        "dungeon_3": dungeon_img3 := pygame.image.load(resource_path("tiles/dungeon_tile3.png")).convert_alpha(), dungeon_img3.set_colorkey((255, 255, 255))),
        "dungeon_4": dungeon_img4 := pygame.image.load(resource_path("tiles/dungeon_tile4.png")).convert_alpha(), dungeon_img4.set_colorkey((255, 255, 255))),
        "dungeon_5": dungeon_img5 := pygame.image.load(resource_path("tiles/dungeon_tile5.png")).convert_alpha(), dungeon_img5.set_colorkey((255, 255, 255))),
        "dungeon_6": dungeon_img6 := pygame.image.load(resource_path("tiles/dungeon_tile6.png")).convert_alpha(), dungeon_img6.set_colorkey((255, 255, 255))),
        "dungeon_7": dungeon_img7 := pygame.image.load(resource_path("tiles/dungeon_tile7.png")).convert_alpha(), dungeon_img7.set_colorkey((255, 255, 255))),
        "dungeon_8": dungeon_img8 := pygame.image.load(resource_path("tiles/dungeon_tile8.png")).convert_alpha(), dungeon_img8.set_colorkey((255, 255, 255))),
        "dungeon_9": dungeon_img9 := pygame.image.load(resource_path("tiles/dungeon_tile9.png")).convert_alpha(), dungeon_img9.set_colorkey((255, 255, 255))),
        "dungeon_10": dungeon_img10 := pygame.image.load(resource_path("tiles/dungeon_tile10.png")).convert_alpha(), dungeon_img10.set_colorkey((255, 255, 255))),
        "dungeon_11": dungeon_img11 := pygame.image.load(resource_path("tiles/dungeon_tile11.png")).convert_alpha(), dungeon_img11.set_colorkey((255, 255, 255))),
        "dungeon_12": dungeon_img12 := pygame.image.load(resource_path("tiles/dungeon_tile12.png")).convert_alpha(), dungeon_img12.set_colorkey((255, 255, 255)))
    }

def Load_Void_Tileset():
        void_img1 := pygame.image.load(resource_path("tiles/void_tile1.png")).convert_alpha(),
        void_img1.set_colorkey((255, 255, 255)),
        void_img2 := pygame.image.load(resource_path("tiles/void_tile2.png")).convert_alpha(),
        void_img2.set_colorkey((255, 255, 255)),
        void_img3 := pygame.image.load(resource_path("tiles/void_tile3.png")).convert_alpha(),
        void_img3.set_colorkey((255, 255, 255)),
        void_img4 := pygame.image.load(resource_path("tiles/void_tile4.png")).convert_alpha(),
        void_img4.set_colorkey((255, 255, 255)),
        void_img5 := pygame.image.load(resource_path("tiles/void_tile5.png")).convert_alpha(),
        void_img5.set_colorkey((255, 255, 255)),
        void_img6 := pygame.image.load(resource_path("tiles/void_tile6.png")).convert_alpha(),
        void_img6.set_colorkey((255, 255, 255)),
        void_img7 := pygame.image.load(resource_path("tiles/void_tile7.png")).convert_alpha(),
        void_img7.set_colorkey((255, 255, 255)),
        void_img8 := pygame.image.load(resource_path("tiles/void_tile8.png")).convert_alpha(),
        void_img8.set_colorkey((255, 255, 255)),
        void_img9 := pygame.image.load(resource_path("tiles/void_tile9.png")).convert_alpha(),
        void_img9.set_colorkey((255, 255, 255)),
        void_img10 := pygame.image.load(resource_path("tiles/void_tile10.png")).convert_alpha(), 
        void_img10.set_colorkey((255, 255, 255)),
        void_img11 := pygame.image.load(resource_path("tiles/void_tile11.png")).convert_alpha(), 
        void_img11.set_colorkey((255, 255, 255)),
        void_img12 := pygame.image.load(resource_path("tiles/void_tile12.png")).convert_alpha(), 
        void_img12.set_colorkey((255, 255, 255)),
        void_img13 := pygame.image.load(resource_path("tiles/void_tile13.png")).convert_alpha(), 
        void_img13.set_colorkey((255, 255, 255)),
        void_img14 := pygame.image.load(resource_path("tiles/void_tile14.png")).convert_alpha(), 
        void_img14.set_colorkey((255, 255, 255))
    return {
        "void_1"
        "void_2"
        "void_3"
        "void_4"
        "void_5"
        "void_6"
        "void_7"
        "void_8"
        "void_9"
        "void_10
        "void_11
        "void_12
        "void_13
        "void_14
    }