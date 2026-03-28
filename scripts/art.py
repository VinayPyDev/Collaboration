import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)


def load_player_idle():
    return {
        "idle_0": pygame.transform.scale(pygame.image.load(resource_path("player_animations/idle/player.png")).convert_alpha(), (150, 150))
    }

def load_player_idle_left():
    return {
        "idle_1": pygame.transform.scale(pygame.image.load(resource_path("player_animations/idle/player_left.png")).convert_alpha(), (150, 150))
    }

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

def load_keys():
    return {
        "key1": pygame.image.load(resource_path("data/sprite-0001.png")).convert_alpha(),
        "key2": pygame.image.load(resource_path("data/sprite-0003.png")).convert_alpha(),
        "key3": pygame.image.load(resource_path("data/sprite-0004.png")).convert_alpha(),
        "key4": pygame.image.load(resource_path("data/sprite-0005.png")).convert_alpha()
    }