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

def load_sunset_bg_full():
    return {
        "sunset": pygame.transform.scale(pygame.image.load(resource_path("data/sunsetbg_full.png")).convert_alpha(), (2900, 720))
    }

def load_dungeon_bg_full():
    return {
        "dungeon": pygame.transform.scale(pygame.image.load(resource_path("data/dungeonbg_full.png")).convert_alpha(), (1900, 720))
    }
