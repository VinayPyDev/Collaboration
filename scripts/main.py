import pygame
import sys

from art import load_player_idle, load_sunset_bg_full, load_dungeon_bg_full
from display import draw_sunset_bg_full, draw_dungeon_bg_full
from menu import main_menu
from text import Awareness_text

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

art = {}
art.update(load_player_idle())
art.update(load_sunset_bg_full())
art.update(load_dungeon_bg_full())

class Player:
    def __init__(self, img, x, y):
        self.image = img
        self.rect = self.image.get_rect()
        self.x = float(x)
        self.y = float(y)
        self.rect.topleft = (self.x, self.y)

player = Player(art["idle_0"], 640, 430)

camera_x = 0

in_dungeon = False
in_sunset = True

player_speed = 150
move_left = False
move_right = False

main_menu()

running = True
while running:
    
    screen.fill((10, 10, 10))

    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_a, pygame.K_LEFT):
                move_left = True
            if event.key in (pygame.K_d, pygame.K_RIGHT):
                move_right = True

            if event.key == pygame.K_ESCAPE:
                main_menu()
                
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_LEFT):
                move_left = False
            if event.key in (pygame.K_d, pygame.K_RIGHT):
                move_right = False

    if move_left:
        player.x -= player_speed * dt
    if move_right:
        player.x += player_speed * dt

    if player.x - camera_x < 200:
        camera_x -= 300 * dt
    if player.x - camera_x > WIDTH - 200:
        camera_x += 300 * dt

    if player.x >= 3200:
        in_dungeon = True

    if not in_dungeon:
        draw_sunset_bg_full(screen, art, camera_x)
    else:
        draw_dungeon_bg_full(screen, art, camera_x)

    if in_sunset == True:
        draw_sunset_bg_full(screen, art, camera_x)

    player.rect.topleft = (int(player.x - camera_x), int(player.y))
    
    screen.blit(player.image, player.rect)
    pygame.display.update()

pygame.quit()
sys.exit()