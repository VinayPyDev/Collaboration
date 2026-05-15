import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def SocialMediaButton():
    return {
        "youtube": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/Youtube.png")).convert_alpha(), (64, 64)),
        "instagram": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/Instagram.png")).convert_alpha(), (64, 64)),
        "facebook": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/FaceBook.png")).convert_alpha(), (64, 64)),
        "twitter": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/Twitter.png")).convert_alpha(), (64, 64)),
    }

def RenderYoutubeButton(screen, art):
    screen.blit(art["youtube"], (300, 656))
def RenderInstagramButton(screen, art):
    screen.blit(art["instagram"], (400, 656))
def RenderFaceBookButton(screen, art):
    screen.blit(art["facebook"], (500, 656))
def RenderTwitterButton(screen, art):
    screen.blit(art["twitter"], (600, 565))

def HoverBar():
    return {
        "if_hovered": pygame.transform.scale(pygame.image.load(resource_path("data/slider.png")).convert_alpha(), (200, 250))
    }
def RenderHoverBar(screen, art):
    screen.blit(art["if_hovered"], (300, 656 - 50))
def RenderHoverBar2(screen, art):
    screen.blit(art["if_hovered"], (400, 656 - 50))
def RenderHoverBar3(screen, art):
    screen.blit(art["if_hovered"], (500, 656 - 50))
def RenderHoverBar4(screen, art):
    screen.blit(art["if_hovered"], (600, 656 - 50))