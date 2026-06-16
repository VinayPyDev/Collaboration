import pygame
import sys
import os

from font import get_font, get_font_BOLD

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def ThanksToDevsScreenText():
    t1 = get_font_BOLD(45).render("THANKS TO", True, (0, 255, 0))
    screen.blit(t1, (400, 40))

    t2 = get_font(45).render("VinayPyDev  LucaArt  Rusty9q1", True, "#FFFFFF")
    t3 = get_font(45).render("DvD777  Oopsi  Neon", True, "#FFFFFF")
    
    screen.blit(t2, (50, 100))
    screen.blit(t3, (50, 230))

def ThanksToDevsScreen():
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    show_key = False
    running = True

    while running:
        screen.fill((0, 0, 0))

        ThanksToDevsScreenText()

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 2000:
            show_key = True

        if show_key:
            press_text = get_font_BOLD(45).render("Press any key to continue", True, (255, 255, 255))
            screen.blit(press_text, press_text.get_rect(center=(600, 650)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if show_key and event.type == pygame.KEYDOWN:
                running = False

        pygame.display.update()
        clock.tick(60)