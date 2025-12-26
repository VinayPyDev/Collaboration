import pygame

def draw_player_idle(screen, art, x, y):
    img = art["idle_0"]
    rect = img.get_rect(center=(x, y))
    screen.blit(img, rect)
    