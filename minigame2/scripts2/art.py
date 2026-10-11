import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def load_keys():
    return {
        "key1": pygame.image.load(resource_path("data/sprite-0001.png")).convert_alpha(),
        "key2": pygame.image.load(resource_path("data/sprite-0003.png")).convert_alpha(),
        "key3": pygame.image.load(resource_path("data/sprite-0004.png")).convert_alpha(),
        "key4": pygame.image.load(resource_path("data/sprite-0005.png")).convert_alpha()
    }
def render_key1(screen, art):
    screen.blit(art["key1"], (105, 0))
def render_key2(screen, art):
    screen.blit(art["key2"], (40, 65))
def render_key3(screen, art):
    screen.blit(art["key3"], (105, 65))
def render_key4(screen, art):
    screen.blit(art["key4"], (170, 65))

