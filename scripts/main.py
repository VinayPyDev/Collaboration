import pygame
import sys

from art import load_player_idle, load_player_idle_left
from art import load_sunset_bg_full, load_dungeon_bg_full, load_sunset_bg_2_full
from display import draw_sunset_bg_full, draw_dungeon_bg_full, draw_sunset_bg_2_full, render_memory_1
from menu import main_menu
from text import Awareness_text
from memory_render import Render_memory_1

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

art = {}
art.update(load_player_idle())
art.update(load_player_idle_left())

art.update(load_sunset_bg_full())
art.update(load_sunset_bg_2_full())

art.update(load_dungeon_bg_full())

Memory_1_frames = Render_memory_1()
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

class Player:
    def __init__(self, img, x, y):
        self.image = img
        self.rect = self.image.get_rect()
        self.x = float(x)
        self.y = float(y)
        self.rect.topleft = (self.x, self.y)

player = Player(art["idle_0"], 640, 430)
player_facing = "right"

camera_x = 0

in_dungeon = True
in_sunset = True
in_sunset_2 = True

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
    
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time

        if frame >= len(Memory_1_frames):
            frame = 0

    if move_left:
        player.x -= player_speed * dt
        player.image = art["idle_1"]
        player_facing = "left"
    if move_right:
        player.x += player_speed * dt
        player.image = art["idle_0"]
        player_facing = "right"

    camera_x = player.x - WIDTH // 2

    if camera_x < 0:
        camera_x = 0
    if player.x < 0:
        player.x = 0

    if player.x >= 3200:
        in_dungeon = True

    if in_dungeon == True:
        draw_dungeon_bg_full(screen, art, camera_x)

    if in_sunset == True:
        draw_sunset_bg_full(screen, art, camera_x)
    if in_sunset_2 == True:
        draw_sunset_bg_2_full(screen, art, camera_x)

    player.rect.topleft = (int(player.x - camera_x), int(player.y))

    if player.x >= 1300 and player.x <= 1320:
        render_memory_1(screen, Memory_1_frames[frame], camera_x)
    
    screen.blit(player.image, player.rect)

    pygame.display.update()

pygame.quit()
sys.exit()