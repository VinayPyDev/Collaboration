import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def Locker():
    return {
        "locker": pygame.image.load(resource_path("data2/locker.png")).convert_alpha()
    }

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

def pin():
    return {
        "normal": pygame.transform.scale2x(pygame.image.load(resource_path("data2/pin.png")).convert_alpha()),
        "breaking": pygame.transform.scale2x(pygame.image.load(resource_path("data2/pin2.png")).convert_alpha()),
        "broken": pygame.transform.scale2x(pygame.image.load(resource_path("data2/pin3.png")).convert_alpha())
    }

def screwdriver():
    return {
        "normal": pygame.transform.scale2x(pygame.image.load(resource_path("data2/screwdriver.png")).convert_alpha()),
        "broken": pygame.transform.scale2x(pygame.image.load(resource_path("data2/screwdriver2.png")).convert_alpha())
    }

def coin():
    return {
        "coin": pygame.transform.scale2x(pygame.image.load(resource_path("data2/coin.png")).convert_alpha())
    }

def filer():
    return {
        "normal": pygame.transform.scale2x(pygame.image.load(resource_path("data2/filer.png")).convert_alpha()),
        "broken": pygame.transform.scale2x(pygame.image.load(resource_path("data2/filer2.png")).convert_alpha())
    }