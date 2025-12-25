import pygame
import sys

from art import load_player_idle
from display import draw_player_idle

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Voices of the Silent Shadows")
clock = pygame.time.Clock()

art = {}
art.update(load_player_idle())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))
    draw_player_idle(screen, art)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
