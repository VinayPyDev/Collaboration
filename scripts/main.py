import pygame
import sys
import os

from art import load_sunset_bg_full, load_dungeon_bg_full, load_sunset_bg_2_full, load_sunset_extra, load_keys, load_void_bg_full
from art import RenderPlayerIdleLeft, RenderPlayerIdleRight, RenderPlayerMoveLeft, RenderPlayerMoveRight
from art import Transition_backgrounds

from display import draw_sunset_bg_full, draw_dungeon_bg_full, draw_sunset_bg_2_full, render_memory_1, render_memory_2, render_memory_3, render_memory_4, render_memory_5, render_memory_6, render_memory_7, render_memory_8, render_memory_9
from display import draw_sunset_bg_extra_full, render_key1, render_key2, render_key3, render_key4, draw_dungeon_bg_full_2, draw_void_bg_full, draw_void_bg_2_full
from display import RenderSunsetToDungeon, RenderDungeonToVoid

from menu import main_menu
from memory_render import Render_memory_1, Render_memory_2, Render_memory_3, Render_memory_4, Render_memory_5, Render_memory_6, Render_memory_7, Render_memory_8, Render_memory_9
from transition import TransitionObj, fade
# from tilesets import Render_Sunrise_Tileset, Render_Dungeon_Tileset, Render_Void_Tileset
from tilesets import Load_Sunrise_Tileset, Load_Dungeon_Tileset, Load_Void_Tileset
from font import get_font
from text import Start_text

# Jumpscares
from jumpscare import Render_jumpscare_1, Render_jumpscare_2, LoadJumpscare1, LoadJumpscare2

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# minigames
from minigame1.scripts1.main import game1
from minigame2.scripts2.main import game2

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# sunset_tilesets = Render_Sunrise_Tileset()
# dungeon_tilesets = Render_Dungeon_Tileset()
# void_tilesets = Render_Void_Tileset()

sunrise_tiles = Load_Sunrise_Tileset()
dungeon_tiles = Load_Dungeon_Tileset()
void_tiles = Load_Void_Tileset()

def load_map(path):
    with open(path + '.txt', 'r') as f:
        data = f.read().splitlines()
    return [list(row) for row in data]

game_map = load_map("map/map")

art = {}

art.update(load_sunset_bg_full())
art.update(load_sunset_bg_2_full())
art.update(load_sunset_extra())
art.update(load_dungeon_bg_full())
art.update(load_void_bg_full())
art.update(load_keys())
art.update(Transition_backgrounds())

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

# Jumpscare anim vars
Jumpscare1_frames = Render_jumpscare_1()
frame_j = 0
last_updatej = pygame.time.get_ticks()
animation_cooldownj = 400

Jumpscare2_frames = Render_jumpscare_2()
frame_j2 = 0
last_updatej = pygame.time.get_ticks()
animation_cooldownj = 400

j1_trigger = False
j2_trigger = False

j1_started = False
j2_started = False

# memory anim vars
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

player_speed = 1500
move_left = False
move_right = False

ground_y = 600
map_end_x = 11000

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
            if event.key == pygame.K_ESCAPE:
                main_menu()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed * dt

    if keys[pygame.K_d]:
        player_x += player_speed * dt

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

    current_time = pygame.time.get_ticks()

    if current_time - last_updatej >= animation_cooldownj:
        last_updatej = current_time

        if j1_trigger:
            frame_j += 1
            if frame_j >= len(Jumpscare1_frames):
                frame_j = 0
                j1_trigger = False

        if j2_trigger:
            frame_j2 += 1
            if frame_j2 >= len(Jumpscare2_frames):
                frame_j2 = 0
                j2_trigger = False
                
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

    if camera_x > map_end_x:
        camera_x = map_end_x
    if player_x > map_end_x:
        player_x = map_end_x
    
    if player_y > ground_y - 150:
        player_y = ground_y - 150

    if player_x >= 2400 and not minigame1_started:
        game1()
        player_x = player_x + 10
        minigame1_started = True

    if player_x >= 6120 and not minigame2_started:
        game2()
        player_x = player_x + 10
        minigame2_started = True

    if minigame1_started:
        move_right = False
        move_left = False
        # minigame1_started = False
    if minigame2_started:
        move_right = False
        move_left = False
        # minigame2_started = False

    if not j1_started and player_x > 9820:
        j1_trigger = True
        j1_started = True

    if not j2_started and player_x > 8210:
        j2_trigger = True
        j2_started = True

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
        RenderSunsetToDungeon(screen, art, camera_x)
    if in_void:
        RenderDungeonToVoid(screen, art, camera_x)
        draw_void_bg_full(screen, art, camera_x)
        draw_void_bg_2_full(screen, art, camera_x)

    if current_bg == "sunset":
        Start_text()   

    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            # SUNRISE TILES
            if tile == "1":
                screen.blit(sunrise_tiles["sun_1"], (x * 48 - camera_x, y * 48))
                tile_rects.append(pygame.Rect(x * 48, y * 48, 48, 48))
            elif tile == "2":
                screen.blit(sunrise_tiles["sun_2"], (x * 50 - camera_x, y * 23))
                tile_rects.append(pygame.Rect(x * 50, y * 23, 50, 23))
            elif tile == "3":
                screen.blit(sunrise_tiles["sun_3"], (x * 18 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 18, y * 18, 18, 18))
            elif tile == "4":
                screen.blit(sunrise_tiles["sun_4"], (x * 18 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 18, y * 18, 18, 18))
            elif tile == "5":
                screen.blit(sunrise_tiles["sun_5"], (x * 18 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 18, y * 18, 18, 18))
            elif tile == "6":
                screen.blit(sunrise_tiles["sun_6"], (x * 18 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 18, y * 18, 18, 18))
            elif tile == "7":
                screen.blit(sunrise_tiles["sun_7"], (x * 17 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 17, y * 18, 17, 18))
            elif tile == "8":
                screen.blit(sunrise_tiles["sun_8"], (x * 17 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 17, y * 18, 17, 18))
            elif tile == "9":
                screen.blit(sunrise_tiles["sun_9"], (x * 17 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 17, y * 18, 17, 18))
            elif tile == "10":
                screen.blit(sunrise_tiles["sun_10"], (x * 17 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 17, y * 18, 17, 18))
            elif tile == "11":
                screen.blit(sunrise_tiles["sun_11"], (x * 65 - camera_x, y * 64))
                tile_rects.append(pygame.Rect(x * 65, y * 64, 65, 64))    
            elif tile == "12":
                screen.blit(sunrise_tiles["sun_12"], (x * 49 - camera_x, y * 47))
                tile_rects.append(pygame.Rect(x * 49, y * 47, 49, 47)) 

            # DUNGEON TILES
            elif tile == "13":
                screen.blit(dungeon_tiles["dungeon_1"], (x * 49 - camera_x, y * 49))
                tile_rects.append(pygame.Rect(x * 49, y * 49, 49, 49))
            elif tile == "14":
                screen.blit(dungeon_tiles["dungeon_2"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "15":
                screen.blit(dungeon_tiles["dungeon_3"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "16":
                screen.blit(dungeon_tiles["dungeon_4"], (x * 20 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 20, y * 18, 20, 18))
            elif tile == "17":
                screen.blit(dungeon_tiles["dungeon_5"], (x * 32 - camera_x, y * 32))
                tile_rects.append(pygame.Rect(x * 32, y * 32, 32, 32))
            elif tile == "18":
                screen.blit(dungeon_tiles["dungeon_6"], (x * 15 - camera_x, y * 47))
                tile_rects.append(pygame.Rect(x * 15, y * 47, 15, 47))
            elif tile == "19":
                screen.blit(dungeon_tiles["dungeon_7"], (x * 48 - camera_x, y * 46))
                tile_rects.append(pygame.Rect(x * 48, y * 46, 48, 46))
            elif tile == "20":
                screen.blit(dungeon_tiles["dungeon_8"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "21":
                screen.blit(dungeon_tiles["dungeon_9"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "22":
                screen.blit(dungeon_tiles["dungeon_10"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "23":
                screen.blit(dungeon_tiles["dungeon_11"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))    
            elif tile == "24":
                screen.blit(dungeon_tiles["dungeon_12"], (x * 63 - camera_x, y * 65))
                tile_rects.append(pygame.Rect(x * 63, y * 65, 63, 65))          
            
            # VOID TILES
            elif tile == "25":
                screen.blit(void_tiles["void_1"], (x * 48 - camera_x, y * 42))
                tile_rects.append(pygame.Rect(x * 48, y * 42, 48, 42))
            elif tile == "26":
                screen.blit(void_tiles["void_2"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "27":
                screen.blit(void_tiles["void_3"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "28":
                screen.blit(void_tiles["void_4"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "29":
                screen.blit(void_tiles["void_5"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "30":
                screen.blit(void_tiles["void_6"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "31":
                screen.blit(void_tiles["void_7"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "32":
                screen.blit(void_tiles["void_8"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "33":
                screen.blit(void_tiles["void_9"], (x * 65 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 65, y * 16, 65, 16))
            elif tile == "34":
                screen.blit(void_tiles["void_10"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "35":
                screen.blit(void_tiles["void_11"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))    
            elif tile == "36":
                screen.blit(void_tiles["void_12"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "37":
                screen.blit(void_tiles["void_13"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))    
            elif tile == "38":
                screen.blit(void_tiles["void_14"], (x * 66 - camera_x, y * 65))
                tile_rects.append(pygame.Rect(x * 66, y * 65, 66, 65))
            x += 1
        y += 1

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
        text_timer = 6400
        fade.start(1500, reverse=False) 
        fade_out_started = True
        current_bg = "dusk"
        sunset_fade_triggered = True

    if player_x >= 6400 and current_bg == "dusk" and in_sunset_2 and not dusk_fade_triggered:
        transition_text_surface = get_font(45).render(dusk_to_dungeon, True, (244, 244, 244))
        transition_text_surface_2 = get_font(45).render(dusk_to_dungeon_2, True, (244, 244, 244))
        text_timer = 4000
        fade.start(1500, reverse=False)
        fade_out_started = True
        current_bg = "dungeon"
        dusk_fade_triggered = True
    
    if player_x >= 9700 and current_bg == "dungeon" and in_dungeon and not dungeon_fade_triggered:
        transition_text_surface = get_font(45).render(dungeon_to_void, True, (244, 244, 244))
        transition_text_surface_2 = get_font(45).render(dungeon_to_void_2, True, (244, 244, 244))
        text_timer = 4000
        fade.start(1500, reverse=False)
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

    if j1_trigger:
        screen.fill((0, 0, 0))
        move_left = False
        move_right = False
        LoadJumpscare1(screen, Jumpscare1_frames[frame_j], (400, 0))
        if frame_j == 50:
            j1_trigger = False
    if j2_trigger:
        screen.fill((0, 0, 0))
        move_left = False
        move_right = False
        LoadJumpscare2(screen, Jumpscare2_frames[frame_j2], (400, 0))
        if frame_j2 == 31:
            j2_trigger = False

    render_key1(screen, art) 
    render_key2(screen, art)
    render_key3(screen, art)
    render_key4(screen, art)

    pygame.display.update()

pygame.quit()
sys.exit()