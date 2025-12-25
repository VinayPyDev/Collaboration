import pygame

def draw_player_idle(screen, art):
    img = art["idle_0"]
    rect = img.get_rect(center=(640, 360))
    screen.blit(img, rect)