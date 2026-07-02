import pygame
import sys
import os

from font import get_font, get_font_BOLD

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def ThanksToDevsScreenText():
    t1 = get_font_BOLD(45).render("THANKS TO", True, (0, 255, 0))
    screen.blit(t1, (400, 20))

    t2 = get_font_BOLD(45).render("VinayPyDev    LucaArt    Rusty9q1", True, "#FFFFFF")
    t3 = get_font_BOLD(45).render("DvD777    Oopsi    Neon Poltergeist", True, "#FFFFFF")
    t4 = get_font_BOLD(45).render("Snes", True, "#FFFFFF")

    screen.blit(t2, (50, 100))
    screen.blit(t3, (50, 230))
    screen.blit(t4, (50, 360))

    sprite0 = pygame.image.load(resource_path("thanks sprites/sprites.png")).convert_alpha()
    sprite1 = pygame.image.load(resource_path("thanks sprites/sprites2.png")).convert_alpha()
    sprite2 = pygame.image.load(resource_path("thanks sprites/sprites4.png")).convert_alpha()
    sprite3 = pygame.image.load(resource_path("thanks sprites/sprites3.png")).convert_alpha()
    sprite4 = pygame.image.load(resource_path("thanks sprites/sprites5.png")).convert_alpha()
    sprite5 = pygame.image.load(resource_path("thanks sprites/sprites6.png")).convert_alpha()
    sprite6 = pygame.image.load(resource_path("thanks sprites/sprites7.png")).convert_alpha()
    sprite7 = pygame.image.load(resource_path("thanks sprites/sprites8.png")).convert_alpha()

    screen.blit(sprite0, (100, 80))
    screen.blit(sprite1, (500, 80))
    screen.blit(sprite2, (900, 80))
    screen.blit(sprite3, (100, 205))
    screen.blit(sprite4, (400, 210))
    screen.blit(sprite5, (860, 210))
    screen.blit(sprite6, (100, 340))

def ThanksToDevsScreen():
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    show_key = False
    running = True

    while running:
        screen.fill((0, 0, 0))

        ThanksToDevsScreenText()

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:
            show_key = True

        if show_key:
            press_text = get_font_BOLD(45).render("Press E key to continue", True, (255, 255, 255))
            screen.blit(press_text, press_text.get_rect(center=(600, 650)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if show_key and event.type == pygame.KEYDOWN:
                running = False

        pygame.display.update()
        clock.tick(60)