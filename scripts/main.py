import pygame
import sys
import os

from art import load_sunset_bg_full, load_dungeon_bg_full, load_sunset_bg_2_full, load_sunset_extra, load_keys, load_void_bg_full
from art import RenderPlayerIdleLeft, RenderPlayerIdleRight, RenderPlayerMoveLeft, RenderPlayerMoveRight

from display import draw_sunset_bg_full, draw_dungeon_bg_full, draw_sunset_bg_2_full, render_memory_1, render_memory_2, render_memory_3, render_memory_4, render_memory_5, render_memory_6, render_memory_7, render_memory_8, render_memory_9
from display import draw_sunset_bg_extra_full, render_key1, render_key2, render_key3, render_key4, draw_dungeon_bg_full_2, draw_void_bg_full, draw_void_bg_2_full

from menu import main_menu
from memory_render import Render_memory_1, Render_memory_2, Render_memory_3, Render_memory_4, Render_memory_5, Render_memory_6, Render_memory_7, Render_memory_8, Render_memory_9
from transition import TransitionObj, fade
from tilesets import Render_Sunrise_Tileset, Render_Dungeon_Tileset, Render_Void_Tileset
from font import get_font
from text import Start_text

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# minigames
from minigame1.scripts1.main import game1
from minigame2.scripts2.main import game2

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

sunset_tilesets = Render_Sunrise_Tileset()
dungeon_tilesets = Render_Dungeon_Tileset()
void_tilesets = Render_Void_Tileset()

def load_map(path):
    with open(path + '.txt', 'r') as f:
        data = f.read().splitlines()
    return [list(row) for row in data]

art = {}

art.update(load_sunset_bg_full())
art.update(load_sunset_bg_2_full())
art.update(load_sunset_extra())

art.update(load_dungeon_bg_full())
art.update(load_void_bg_full())

art.update(load_keys())

# minigames
minigame1_started = False
minigame2_started = False

transition_text = ""
sunset_to_dusk = "The sun has descended and dusk holds its crown"
dusk_to_dungeon = "The dusk faded away and now night is in its "
dusk_to_dungeon_2 = "prime"
dungeon_to_void = "The innocence has been stabbed and has turned"
dungeon_to_void_2 = " to the path of vengeance"

sunset_fade_triggered = False
dusk_fade_triggered = False
dungeon_fade_triggered = False

fade_out_started = False

text_timer = 0
text_surf = None

current_bg = "sunset"

Memory_1_frames = Render_memory_1()
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_2_frames = Render_memory_2()
frame2 = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_3_frames = Render_memory_3()
frame3 = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_4_frames = Render_memory_4()
frame4 = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_5_frames = Render_memory_5()
frame5 = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_6_frames = Render_memory_6()
frame6 = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_7_frames = Render_memory_7()
frame7 = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_8_frames = Render_memory_8()
frame8 = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

Memory_9_frames = Render_memory_9()
frame9 = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100

memory1Trigger = False
memory2Trigger = False
memory3Trigger = False
memory4Trigger = False
memory5Trigger = False
memory6Trigger = False
memory7Trigger = False
memory8Trigger = False
memory9Trigger = False

player_x = 640
player_y = 386

idle_right_frames = RenderPlayerIdleRight()
idle_left_frames = RenderPlayerIdleLeft()

player_facing = "right"
current_frame = 0
frame_timer = 0
frame_cooldown = 100
current_player_img = idle_right_frames[0]

move_right_frames = RenderPlayerMoveRight()
move_left_frames = RenderPlayerMoveLeft()

camera_x = 0

in_dungeon = True
in_sunset = True
in_sunset_2 = True
in_void = True

player_speed = 1050
move_left = False
move_right = False

ground_y = 600

text_displayed = False

main_menu()

running = True
while running:
    
    mouse_pos = pygame.mouse.get_pos()
    screen.fill((10, 10, 10))

    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True

            if event.key == pygame.K_ESCAPE:
                main_menu()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        last_update = current_time
        frame += 1
        frame2 += 1
        frame3 += 1
        frame4 += 1
        frame5 += 1
        frame6 += 1
        frame7 += 1
        frame8 += 1
        frame9 += 1

        if frame >= len(Memory_1_frames):
            frame = 0
        if frame2 >= len(Memory_2_frames):
            frame2 = 0
        if frame3 >= len(Memory_3_frames):
            frame3 = 0
        if frame4 >= len(Memory_4_frames):
            frame4 = 0
        if frame5 >= len(Memory_5_frames):
            frame5 = 0
        if frame6 >= len(Memory_6_frames):
            frame6 = 0
        if frame7 >= len(Memory_7_frames):
            frame7 = 0
        if frame8 >= len(Memory_8_frames):
            frame8 = 0
        if frame9 >= len(Memory_9_frames):
            frame9 = 0

    if move_left:
        player_x -= player_speed * dt
        player_facing = "left"
    if move_right:
        player_x += player_speed * dt
        player_facing = "right"

    frame_timer += dt * 1000
    if frame_timer >= frame_cooldown:
        frame_timer = 0
        current_frame += 1

        if player_facing == "right":
            if current_frame >= len(idle_right_frames):
                current_frame = 0
            if current_frame >= len(move_right_frames):
                current_frame = 0
        else:
            if current_frame >= len(idle_left_frames):
                current_frame = 0
            if current_frame >= len(move_left_frames):
                current_frame = 0

    camera_x = player_x - WIDTH // 2

    if camera_x < 0:
        camera_x = 0
    if player_x < 0:
        player_x = 0
    
    if player_y > ground_y - 150:
        player_y = ground_y - 150

    if player_x >= 2400 and not minigame1_started:
        result = game1()
        print(result)
        minigame1_started = True

    if player_x >= 4200 and not minigame2_started:
        result = game2()
        print(result)
        minigame2_started = True

    if not memory1Trigger and player_x >= 1300:
        memory1Trigger = True
    if not memory2Trigger and player_x >= 2700:
        memory2Trigger = True
    if not memory3Trigger and player_x >= 4000:
        memory3Trigger = True
    if not memory4Trigger and player_x >= 5300:
        memory4Trigger = True
    if not memory5Trigger and player_x >= 6400:
        memory5Trigger = True
    if not memory6Trigger and player_x >= 7300:
        memory6Trigger = True
    if not memory7Trigger and player_x >= 8450:
        memory7Trigger = True
    if not memory8Trigger and player_x >= 9523:
        memory8Trigger = True 
    if not memory9Trigger and player_x >= 10750:
        memory9Trigger = True

    if in_dungeon:
        draw_dungeon_bg_full(screen, art, camera_x)
        draw_dungeon_bg_full_2(screen, art, camera_x)
    if in_sunset:
        draw_sunset_bg_full(screen, art, camera_x)
        draw_sunset_bg_extra_full(screen, art, camera_x)
    if in_sunset_2:
        draw_sunset_bg_2_full(screen, art, camera_x)
    if in_void:
        draw_void_bg_full(screen, art, camera_x)
        draw_void_bg_2_full(screen, art, camera_x)

    if current_bg == "sunset":
        Start_text()

    if player_facing == "right":
        current_player_img = idle_right_frames[current_frame]
    elif player_facing == "left":
        current_player_img = idle_left_frames[current_frame]

    if player_facing == "right" and move_right:
        current_player_img = move_right_frames[current_frame]
    elif player_facing == "left" and move_left:
        current_player_img = move_left_frames[current_frame]

    if memory1Trigger:
        render_memory_1(screen, Memory_1_frames[frame], camera_x)
    if memory2Trigger:
        render_memory_2(screen, Memory_2_frames[frame2], camera_x)
    if memory3Trigger:
        render_memory_3(screen, Memory_3_frames[frame3], camera_x)
    if memory4Trigger:
        render_memory_4(screen, Memory_4_frames[frame4], camera_x)
    if memory5Trigger:
        render_memory_5(screen, Memory_5_frames[frame5], camera_x)
    if memory6Trigger:
        render_memory_6(screen, Memory_6_frames[frame6], camera_x)
    if memory7Trigger:
        render_memory_7(screen, Memory_7_frames[frame7], camera_x) 
    if memory8Trigger:
        render_memory_8(screen, Memory_8_frames[frame8], camera_x)
    if memory9Trigger:
        render_memory_9(screen, Memory_9_frames[frame9], camera_x)   

    screen.blit(current_player_img, (int(player_x - camera_x), int(player_y)))

    fade.update(dt)
    fade.draw(screen)
    # Done(TODO): remove the 3000, reverse=True and add a auto-reversal to TransitionObj in trasition.py
    if player_x >= 2600 and current_bg == "sunset" and in_sunset and not sunset_fade_triggered:
        transition_text_surface = get_font(45).render(sunset_to_dusk, True, (244, 244, 244))
        transition_text_surface_2 = get_font(45).render(" ", True, (244, 244, 244))
        text_timer = 3000
        fade.start(3000, reverse=False) 
        fade_out_started = True
        current_bg = "dusk"
        sunset_fade_triggered = True

    if player_x >= 5645 and current_bg == "dusk" and in_sunset_2 and not dusk_fade_triggered:
        transition_text_surface = get_font(45).render(dusk_to_dungeon, True, (244, 244, 244))
        transition_text_surface_2 = get_font(45).render(dusk_to_dungeon_2, True, (244, 244, 244))
        text_timer = 8000
        fade.start(3000, reverse=False)
        fade_out_started = True
        current_bg = "dungeon"
        dusk_fade_triggered = True
    
    if player_x >= 8700 and current_bg == "dungeon" and in_dungeon and not dungeon_fade_triggered:
        transition_text_surface = get_font(45).render(dungeon_to_void, True, (244, 244, 244))
        transition_text_surface_2 = get_font(45).render(dungeon_to_void_2, True, (244, 244, 244))
        text_timer = 8000
        fade.start(3000, reverse=False)
        fade_out_started = True
        current_bg = "void"
        dungeon_fade_triggered = True

    if fade_out_started and fade.val >= 255 and not text_displayed:
        text_displayed = True

    if text_displayed and text_timer > 0 and transition_text_surface is not None:
        screen.blit(transition_text_surface, (10, 360))
        text_timer -= int(dt * 1000)
    if text_displayed and text_timer > 0 and transition_text_surface_2 is not None:
        screen.blit(transition_text_surface_2, (10, 460))
        text_timer -= int(dt * 1000)

    render_key1(screen, art) 
    render_key2(screen, art)
    render_key3(screen, art)
    render_key4(screen, art)

    pygame.display.update()

pygame.quit()
sys.exit()