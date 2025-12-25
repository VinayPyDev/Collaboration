import pygame

def load_player_idle():
    return {
        "idle_0": pygame.transform.scale(pygame.image.load("data/player_animations/idle/player.png").convert_alpha(), (150, 150))
    }
