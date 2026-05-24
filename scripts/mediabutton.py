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
        "youtube": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/youtube-scaled.png")).convert_alpha(), (150, 150)),
        "instagram": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/instagram-scaled.png")).convert_alpha(), (150, 150)),
        "facebook": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/facebook-scaled.png")).convert_alpha(), (150, 150)),
        "twitter": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/x-scaled.png")).convert_alpha(), (150, 150)),
        "itch.io": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/itch-scaled.png")).convert_alpha(), (150, 150)),
        "steam": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/steam-scaled.png")).convert_alpha(), (150, 150)),
        "tiktok": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/tiktok-scaled1.png")).convert_alpha(), (150, 150)),
        "twitch": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/twitch-scaled.png")).convert_alpha(), (150, 150))
    }

def SocialMediaButtonShrinked():
    return {
        "youtube_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/youtube-scaled.png")).convert_alpha(), (120, 120)),
        "instagram_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/instagram-scaled.png")).convert_alpha(), (120, 120)),
        "facebook_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/facebook-scaled.png")).convert_alpha(), (120, 120)),
        "twitter_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/x-scaled.png")).convert_alpha(), (120, 120)),
        "itch.io_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/itch-scaled.png")).convert_alpha(), (120, 120)),
        "steam_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/steam-scaled.png")).convert_alpha(), (120, 120)),
        "tiktok_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/tiktok-scaled1.png")).convert_alpha(), (120, 120)),
        "twitch_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/twitch-scaled.png")).convert_alpha(), (120, 120))
    }

def RenderYoutubeButton(screen, art):
    screen.blit(art["youtube"], (0, 600))
def RenderInstagramButton(screen, art):
    screen.blit(art["instagram"], (150, 600))
def RenderFaceBookButton(screen, art):
    screen.blit(art["facebook"], (300, 600))
def RenderTwitterButton(screen, art):
    screen.blit(art["twitter"], (450, 600))
def RenderItchIoButton(screen, art):
    screen.blit(art["itch.io"], (600, 600))
def RenderSteamButton(screen, art):
    screen.blit(art["steam"], (750, 600))
def RenderTikTokButton(screen, art):
    screen.blit(art["tiktok"], (900, 600))
def RenderTwitch(screen, art):
    screen.blit(art["twitch"], (1050, 600))

def HoverBar():
    return {
        "if_hovered": pygame.transform.scale(pygame.image.load(resource_path("data/slider.png")).convert_alpha(), (500, 650))
    }
def RenderHoverBar(screen, art):
    screen.blit(art["if_hovered"], (0, 626 - 600))
def RenderHoverBar2(screen, art):
    screen.blit(art["if_hovered"], (150, 626 - 600))
def RenderHoverBar3(screen, art):
    screen.blit(art["if_hovered"], (300, 626 - 600))
def RenderHoverBar4(screen, art):
    screen.blit(art["if_hovered"], (450, 626 - 600))
def RenderHoverBar5(screen, art):
    screen.blit(art["if_hovered"], (600, 626 - 600))
def RenderHoverBar6(screen, art):
    screen.blit(art["if_hovered"], (750, 626 - 600))
def RenderHoverBar7(screen, art):
    screen.blit(art["if_hovered"], (900, 626 - 600))
def RenderHoverBar8(screen, art):
    screen.blit(art["if_hovered"], (1050, 626 - 600))