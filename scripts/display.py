import pygame

def draw_player_idle(screen, art, x, y):
    img = art["idle_0"]
    rect = img.get_rect(center=(x, y))
    screen.blit(img, rect)
    
def draw_sunset_bg_full(screen, art, camera_x):
    screen.blit(art["sunset"], (-camera_x, -150))

def draw_dungeon_bg_full(screen, art, camera_x):
    screen.blit(art["dungeon"], (3200 - camera_x, -150))
