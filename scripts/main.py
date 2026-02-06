import pygame
import sys

from art import load_player_idle, load_player_idle_left
from art import load_sunset_bg_full, load_dungeon_bg_full, load_sunset_bg_2_full
from display import draw_sunset_bg_full, draw_dungeon_bg_full, draw_sunset_bg_2_full, render_memory_1, render_memory_2, render_memory_3, render_memory_4, render_memory_5, render_memory_6, render_memory_7
from menu import main_menu
from text import Awareness_text
from memory_render import Render_memory_1, Render_memory_2, Render_memory_3, Render_memory_4, Render_memory_5, Render_memory_6, Render_memory_7

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

Memory_2_frames = Render_memory_2()
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_3_frames = Render_memory_3()
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_4_frames = Render_memory_4()
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_5_frames = Render_memory_5()
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_6_frames = Render_memory_6()
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_7_frames = Render_memory_7()
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

memory1Trigger = False
memory2Trigger = False
memory3Trigger = False
memory4Trigger = False
memory5Trigger = False
memory6Trigger = False
memory7Trigger = False

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

        if frame >= len(Memory_2_frames):
            frame = 0

        if frame >= len(Memory_3_frames):
            frame = 0
        
        if frame >= len(Memory_4_frames):
            frame = 0
        
        if frame >= len(Memory_5_frames):
            frame = 0
            
        if frame >= len(Memory_6_frames):
            frame = 0

        if frame >= len(Memory_7_frames):
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

    if not memory1Trigger and player.x >= 1300:
        memory1Trigger = True

    if not memory2Trigger and player.x >= 2700:
        memory2Trigger = True

    if not memory3Trigger and player.x >= 4000:
        memory3Trigger = True
    
    if not memory4Trigger and player.x >= 5300:
        memory4Trigger = True
    
    if not memory5Trigger and player.x >= 6400:
        memory5Trigger = True

    if not memory6Trigger and player.x >= 7300:
        memory6Trigger = True

    if not memory7Trigger and player.x >= 8450:
        memory7Trigger = True

    if player.x >= 3200:
        in_dungeon = True

    if in_dungeon == True:
        draw_dungeon_bg_full(screen, art, camera_x)

    if in_sunset == True:
        draw_sunset_bg_full(screen, art, camera_x)
    if in_sunset_2 == True:
        draw_sunset_bg_2_full(screen, art, camera_x)

    player.rect.topleft = (int(player.x - camera_x), int(player.y))

    if memory1Trigger:
        render_memory_1(screen, Memory_1_frames[frame], camera_x)

    if memory2Trigger:
        render_memory_2(screen, Memory_2_frames[frame], camera_x)

    if memory3Trigger:
        render_memory_3(screen, Memory_3_frames[frame], camera_x)

    if memory4Trigger:
        render_memory_4(screen, Memory_4_frames[frame], camera_x)

    if memory5Trigger:
        render_memory_5(screen, Memory_5_frames[frame], camera_x)

    if memory6Trigger:
        render_memory_6(screen, Memory_6_frames[frame], camera_x)

    if memory7Trigger:
        render_memory_7(screen, Memory_7_frames[frame], camera_x)

    screen.blit(player.image, player.rect)

    pygame.display.update()

pygame.quit()
sys.exit()