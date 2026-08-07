import pygame
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def PauseImg():
    return {
        "img": pygame.image.load(resource_path("data 2/pause.png")).convert_alpha()
    }