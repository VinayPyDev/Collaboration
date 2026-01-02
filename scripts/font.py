import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def get_font(size):
    return pygame.font.Font(resource_path("font/PixeloidMono.ttf"), size)

def get_font_BOLD(size):
    return pygame.font.Font(resource_path("font/PixeloidSans-Bold.ttf"), size)
