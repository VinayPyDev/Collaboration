import pygame
import sys
import os

# [additional memory tracking]
import psutil

# [Function imports]
from art import load_sunset_bg_full, load_dungeon_bg_full, load_sunset_bg_2_full, load_sunset_extra, load_keys, load_void_bg_full
from art import RenderPlayerIdleLeft, RenderPlayerIdleRight, RenderPlayerMoveLeft, RenderPlayerMoveRight
from art import Transition_backgrounds, LoadPage, LoadCollisionPage

from display import draw_sunset_bg_full, draw_dungeon_bg_full, draw_sunset_bg_2_full, render_memory_1, render_memory_2, render_memory_3, render_memory_4, render_memory_5, render_memory_6, render_memory_7, render_memory_8, render_memory_9
from display import draw_sunset_bg_extra_full, render_key1, render_key2, render_key3, render_key4, draw_dungeon_bg_full_2, draw_void_bg_full, draw_void_bg_2_full, draw_void_bg_3_full
from display import RenderSunsetToDungeon, RenderDungeonToVoid

from menu import main_menu
from memory_render import Render_memory_1, Render_memory_2, Render_memory_3, Render_memory_4, Render_memory_5, Render_memory_6, Render_memory_7, Render_memory_8, Render_memory_9
from transition import TransitionObj, fade
from tilesets import Load_Sunrise_Tileset, Load_Dungeon_Tileset, Load_Void_Tileset
from font import *
from text import Start_text, Awareness_text

from MemoryLoader import MemoryAnimationLoader

from key import RenderKeyA, RenderKeyS, RenderKeyD, RenderKeyW, LoadKeyA, LoadKeyD, LoadKeyS, LoadKeyW
from key import KeyA, KeyW, KeyS, KeyD, KeyAnimation
from art import PauseImg, PauseMenu
from display import RenderPausedMenu

from music import MenuTrack

# Jumpscares
from jumpscare import jumpscare_1_data, jumpscare_2_data

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# minigames
from minigame1.scripts1.main import game1
from minigame1.scripts1.main import *
from minigame2.scripts2.main import game2
from minigame2.scripts2.main import *
from minigame2.scripts2 import main as minigame_2
from minigame3.scripts3.main import game3
from minigame3.scripts3.main import *
    
from minigame2.scripts2.main import has_no_options

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE | pygame.SCALED)
clock = pygame.time.Clock()

# [Font re-implementation due to some file issues]
def get_font_BOLD(size):
    return pygame.font.Font(resource_path("font/PixeloidSans-Bold.ttf"), size)
def get_font_BKANT(size):
    return pygame.font.Font(resource_path("font/BKANT.TTF"), size)
def get_font(size):
    return pygame.font.Font(resource_path("font/PixeloidSans.ttf"), size)

sunrise_tiles = Load_Sunrise_Tileset()
dungeon_tiles = Load_Dungeon_Tileset()
void_tiles = Load_Void_Tileset()

def load_map(path):
    with open(path + '.txt', 'r') as f:
        data = f.read().splitlines()
    return [list(row) for row in data]
game_map = load_map("map/map2")

art = {}

art.update(load_sunset_bg_full())
art.update(load_sunset_bg_2_full())
art.update(load_sunset_extra())
art.update(load_dungeon_bg_full())
art.update(load_void_bg_full())
art.update(load_keys())
art.update(Transition_backgrounds())
art.update(LoadCollisionPage())
art.update(LoadPage())
art.update(PauseImg())
art.update(PauseMenu())

# minigames
minigame1_started = False
minigame2_started = False
minigame3_started = False

transition_text = ""
sunset_to_dusk = "The sun has descended and dusk holds i"
sunset_to_dusk_2 = "- ts crown"
dusk_to_dungeon = "The dusk faded away and now night is in its "
dusk_to_dungeon_2 = "prime"
dungeon_to_void = "The innocence has been stabbed and has tu"
dungeon_to_void_2 = " rned to the path of corruption"

sunset_fade_triggered = False
dusk_fade_triggered = False
dungeon_fade_triggered = False

fade_out_started = False

text_timer = 0
text_surf = None

current_bg = "sunset"

# page vars
page_pick = art["page_pick"]
not_picked = True

page_pick_pos = [
    (500, 540),
    (1540, 540),
    (3000, 540),
    (4946, 540),
    (6732, 540),
    (7404, 540),
]

picked_page_1 = False
picked_page_2 = False
picked_page_3 = False
picked_page_4 = False
picked_page_5 = False
picked_page_6 = False

page_opened = 0

page_pick_rects = []

for pos in page_pick_pos:
    page_pick_rects.append(page_pick.get_rect(center=pos))

page_1 = art["page_1"]
page_2 = art["page_2"]
page_3 = art["page_3"]
page_4 = art["page_4"]
page_5 = art["page_5"]
page_6 = art["page_6"]

page_1_rect = page_pick_rects[0]
page_2_rect = page_pick_rects[1]
page_3_rect = page_pick_rects[2]
page_4_rect = page_pick_rects[3]
page_5_rect = page_pick_rects[4]
page_6_rect = page_pick_rects[5]

# text
pick_txt = get_font_BOLD(45).render("Press E", True, (0, 0, 0))

# [Key anim vars]
key_pressed_a = False
key_pressed_s = False
key_pressed_d = False
key_pressed_w = False

keys_manager = [
    KeyAnimation(RenderKeyA(), LoadKeyA, (10, 30), pygame.K_a),
    KeyAnimation(RenderKeyS(), LoadKeyS, (77, 30), pygame.K_s),
    KeyAnimation(RenderKeyD(), LoadKeyD, (140, 30), pygame.K_d),
    KeyAnimation(RenderKeyW(), LoadKeyW, (75, -35), pygame.K_w),
]

# Jumpscare anim vars
frame_j = 0
last_updatej = pygame.time.get_ticks()
animation_cooldownj = 400

frame_j2 = 0
last_updatej = pygame.time.get_ticks()
animation_cooldownj = 400

j1_trigger = False
j2_trigger = False

j1_started = False
j2_started = False

# [memory anim vars]
memory_manager = [
    MemoryAnimationLoader(Render_memory_1(), render_memory_1, trigger_x=1260),
    MemoryAnimationLoader(Render_memory_2(), render_memory_2, trigger_x=3450),
    MemoryAnimationLoader(Render_memory_3(), render_memory_3, trigger_x=4000),
    MemoryAnimationLoader(Render_memory_4(), render_memory_4, trigger_x=5240),
    MemoryAnimationLoader(Render_memory_5(), render_memory_5, trigger_x=6234),
    MemoryAnimationLoader(Render_memory_6(), render_memory_6, trigger_x=7040),
    MemoryAnimationLoader(Render_memory_7(), render_memory_7, trigger_x=8158),
    MemoryAnimationLoader(Render_memory_8(), render_memory_8, trigger_x=9328),
    MemoryAnimationLoader(Render_memory_9(), render_memory_9, trigger_x=11750),
]

# player vars
player_x = 200
player_y = 386

idle_right_frames = RenderPlayerIdleRight()
idle_left_frames = RenderPlayerIdleLeft()

player_facing = "right"
current_frame = 0
frame_timer = 0
frame_cooldown = 100
current_player_img = idle_right_frames[0]
player_rect = current_player_img.get_rect(topleft=(player_x, player_y))

move_right_frames = RenderPlayerMoveRight()
move_left_frames = RenderPlayerMoveLeft()

# world vars
camera_x = 0

in_dungeon = True
in_sunset = True
in_sunset_2 = True
in_void = True

# pause button var
pause_btn_rect = art["img"].get_rect(center=(1230 - camera_x, 50))
paused = False

player_speed = 1500
move_left = False
move_right = False

ground_y = 600
map_end_x = 18600

text_displayed = False

surface1 = pygame.Surface((6396, 220))
surface1_rect = pygame.Rect(0, 612, 6396, 220)

main_menu()

running = True
while running:
    
    mouse_pos = pygame.mouse.get_pos()
    screen.fill((10, 10, 10))

    current_page = 0
    for i, rect in enumerate(page_pick_rects):
        if player_rect.colliderect(rect):
            current_page = i + 1
            break

    player_rect.topleft = (player_x, player_y)

    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_btn_rect.collidepoint(event.pos):
                paused = True
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main_menu()
            if event.key == pygame.K_e:
                if page_opened != 0:
                    page_opened = 0
                elif current_page != 0:
                    page_opened = current_page

    if pygame.mouse.get_just_pressed()[0]:
        print(mouse_pos)

    keys = pygame.key.get_pressed()

    key_pressed_a = keys[pygame.K_a]
    key_pressed_s = keys[pygame.K_s]
    key_pressed_d = keys[pygame.K_d]
    key_pressed_w = keys[pygame.K_w]

    move_left = False
    move_right = False

    if key_pressed_a:
        player_x -= player_speed * dt
        move_left = True
        player_facing = "left"

    if key_pressed_d:
        player_x += player_speed * dt
        move_right = True
        player_facing = "right"

    # print(round(player_x))

    if key_pressed_s:
        pass

    if key_pressed_w:
        pass

    current_time = pygame.time.get_ticks()
    if current_time - last_updatej >= animation_cooldownj:
        last_updatej = current_time

        if j1_trigger:
            frame_j += 1
            if frame_j >= jumpscare_1_data.total_frames:
                frame_j = 0
                j1_trigger = False

        if j2_trigger:
            frame_j2 += 1
            if frame_j2 >= jumpscare_2_data.total_frames:
                frame_j2 = 0
                j2_trigger = False
        
    if player_rect.colliderect(page_pick_rects[0]) and not picked_page_1:
        text_of_page_1 = True
    if player_rect.colliderect(page_pick_rects[1]) and not picked_page_2:    
        text_of_page_2 = True
    if player_rect.colliderect(page_pick_rects[2]) and not picked_page_3:
        text_of_page_3 = True
    if player_rect.colliderect(page_pick_rects[3]) and not picked_page_4:
        text_of_page_4 = True
    if player_rect.colliderect(page_pick_rects[4]) and not picked_page_5:
        text_of_page_5 = True
    if player_rect.colliderect(page_pick_rects[5]) and not picked_page_6:
        text_of_page_6 = True

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

    if player_x >= 2230 and not minigame1_started:
        game1()
        player_x = player_x + 10
        minigame1_started = True
        move_left = False
        move_right = False

    if player_x >= 8343 and not minigame2_started:
        game2(screen)
        player_x = player_x + 10
        minigame2_started = True
        move_left = False
        move_right = False

    if player_x >= 14296 and not minigame3_started:
        game3(screen)
        player_x = player_x + 10
        minigame3_started = True
        move_left = False
        move_right = False

    if minigame2_started and minigame_2.has_no_options and player_x >=8343:
        if not j2_trigger:
            j2_trigger = True
        if not j2_started:
            j2_started = True

    if not j1_started and player_x > 16865:
        j1_trigger = True
        j1_started = True

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
        draw_void_bg_3_full(screen, art, camera_x)

    if not picked_page_1:
        screen.blit(page_pick, (page_pick_rects[0].x - camera_x, page_pick_rects[0].y))
    if not picked_page_2:
        screen.blit(page_pick, (page_pick_rects[1].x - camera_x, page_pick_rects[1].y))
    if not picked_page_3:
        screen.blit(page_pick, (page_pick_rects[2].x - camera_x, page_pick_rects[2].y))
    if not picked_page_4:
        screen.blit(page_pick, (page_pick_rects[3].x - camera_x, page_pick_rects[3].y))
    if not picked_page_5:
        screen.blit(page_pick, (page_pick_rects[4].x - camera_x, page_pick_rects[4].y))
    if not picked_page_6:
        screen.blit(page_pick, (page_pick_rects[5].x - camera_x, page_pick_rects[5].y))

    if current_bg == "sunset" or current_bg == "dusk" or current_bg == "dungeon" or current_bg == "void":
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
            elif tile == "a":
                screen.blit(sunrise_tiles["sun_10"], (x * 17 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 17, y * 18, 17, 18))
            elif tile == "b":
                screen.blit(sunrise_tiles["sun_11"], (x * 65 - camera_x, y * 64))
                tile_rects.append(pygame.Rect(x * 65, y * 64, 65, 64))    
            elif tile == "c":
                screen.blit(sunrise_tiles["sun_12"], (x * 49 - camera_x, y * 47))
                tile_rects.append(pygame.Rect(x * 49, y * 47, 49, 47)) 

            # DUNGEON TILES
            elif tile == "d":
                screen.blit(dungeon_tiles["dungeon_1"], (x * 49 - camera_x, y * 49))
                tile_rects.append(pygame.Rect(x * 49, y * 49, 49, 49))
            elif tile == "e":
                screen.blit(dungeon_tiles["dungeon_2"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "f":
                screen.blit(dungeon_tiles["dungeon_3"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "g":
                screen.blit(dungeon_tiles["dungeon_4"], (x * 20 - camera_x, y * 18))
                tile_rects.append(pygame.Rect(x * 20, y * 18, 20, 18))
            elif tile == "h":
                screen.blit(dungeon_tiles["dungeon_5"], (x * 32 - camera_x, y * 32))
                tile_rects.append(pygame.Rect(x * 32, y * 32, 32, 32))
            elif tile == "i":
                screen.blit(dungeon_tiles["dungeon_6"], (x * 15 - camera_x, y * 47))
                tile_rects.append(pygame.Rect(x * 15, y * 47, 15, 47))
            elif tile == "j":
                screen.blit(dungeon_tiles["dungeon_7"], (x * 48 - camera_x, y * 46))
                tile_rects.append(pygame.Rect(x * 48, y * 46, 48, 46))
            elif tile == "k":
                screen.blit(dungeon_tiles["dungeon_8"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "l":
                screen.blit(dungeon_tiles["dungeon_9"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "m":
                screen.blit(dungeon_tiles["dungeon_10"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "n":
                screen.blit(dungeon_tiles["dungeon_11"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))    
            elif tile == "o":
                screen.blit(dungeon_tiles["dungeon_12"], (x * 63 - camera_x, y * 65))
                tile_rects.append(pygame.Rect(x * 63, y * 65, 63, 65))          
            
            # VOID TILES
            elif tile == "p":
                screen.blit(void_tiles["void_1"], (x * 48 - camera_x, y * 42))
                tile_rects.append(pygame.Rect(x * 48, y * 42, 48, 42))
            elif tile == "q":
                screen.blit(void_tiles["void_2"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "r":
                screen.blit(void_tiles["void_3"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "s":
                screen.blit(void_tiles["void_4"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "t":
                screen.blit(void_tiles["void_5"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "u":
                screen.blit(void_tiles["void_6"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "v":
                screen.blit(void_tiles["void_7"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "w":
                screen.blit(void_tiles["void_8"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "x":
                screen.blit(void_tiles["void_9"], (x * 65 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 65, y * 16, 65, 16))
            elif tile == "y":
                screen.blit(void_tiles["void_10"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "z":
                screen.blit(void_tiles["void_11"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))    
            elif tile == ";":
                screen.blit(void_tiles["void_12"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            elif tile == "-":
                screen.blit(void_tiles["void_13"], (x * 16 - camera_x, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))    
            elif tile == "+":
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

    current_time = pygame.time.get_ticks()

    for mem_anim in memory_manager:
        mem_anim.update(current_time, player_x)
        mem_anim.draw(screen, camera_x)

    if not move_left:
        current_player_img != move_left_frames[current_frame]

    if not move_right:
        current_player_img != move_right_frames[current_frame]

    if move_left or move_right:
        screen.blit(current_player_img, (int(player_x - camera_x), int(player_y+35)))
    else:
        screen.blit(current_player_img, (int(player_x - camera_x), int(player_y)))

    screen.blit(art["img"], pause_btn_rect)

    fade.update(dt)
    fade.draw(screen)
    # Done(TODO): remove the 3000, reverse=True and add a auto-reversal to TransitionObj in trasition.py
    if player_x >= 2600 and current_bg == "sunset" and in_sunset and not sunset_fade_triggered:
        transition_text_surface = get_font_BOLD(45).render(sunset_to_dusk, True, (244, 244, 244))
        transition_text_surface_2 = get_font_BOLD(45).render(sunset_to_dusk_2, True, (244, 244, 244))
        text_timer = 3000
        fade.start(1500, reverse=False) 
        fade_out_started = True
        current_bg = "dusk"
        sunset_fade_triggered = True

    if player_x >= 6400 and current_bg == "dusk" and in_sunset_2 and not dusk_fade_triggered:
        transition_text_surface = get_font_BOLD(45).render(dusk_to_dungeon, True, (244, 244, 244))
        transition_text_surface_2 = get_font_BOLD(45).render(dusk_to_dungeon_2, True, (244, 244, 244))
        text_timer = 8000
        fade.start(1500, reverse=False)
        fade_out_started = True
        current_bg = "dungeon"
        dusk_fade_triggered = True
    
    if player_x >= 11578 and current_bg == "dungeon" and in_dungeon and not dungeon_fade_triggered:
        transition_text_surface = get_font_BOLD(45).render(dungeon_to_void, True, (244, 244, 244))
        transition_text_surface_2 = get_font_BOLD(45).render(dungeon_to_void_2, True, (244, 244, 244))
        text_timer = 11000
        fade.start(1500, reverse=False)
        fade_out_started = True
        current_bg = "void"
        dungeon_fade_triggered = True

    if fade_out_started and fade.val >= 255 and not text_displayed:
        text_displayed = True

    if text_displayed and text_timer > 0 and transition_text_surface is not None:
        screen.blit(transition_text_surface, (10, 260))
        text_timer -= int(dt * 1000)
    if text_displayed and text_timer > 0 and transition_text_surface_2 is not None:
        screen.blit(transition_text_surface_2, (100, 360))
        text_timer -= int(dt * 1000)

    screen.blit(RenderKeyA()[0], (10, 30))
    screen.blit(RenderKeyS()[0], (77, 30))
    screen.blit(RenderKeyD()[0], (140, 30))
    screen.blit(RenderKeyW()[0], (75, -35))

    pressed_keys = pygame.key.get_pressed()
    for key_anim in keys_manager:
            key_anim.update(current_time, pressed_keys)
            key_anim.draw(screen)
    
    if page_opened == 1:
        screen.blit(page_1, (0, 0))
    if page_opened == 2:
        screen.blit(page_2, (0, 0))
    if page_opened == 3:
        screen.blit(page_3, (0, 0))
    if page_opened == 4:
        screen.blit(page_4, (0, 0))
    if page_opened == 5:
        screen.blit(page_5, (0, 0))
    if page_opened == 6:
        screen.blit(page_6, (0, 0))

    if current_page != 0 and page_opened == 0:
        screen.blit(pick_txt, (player_x - camera_x, player_y - 100))

    if player_x >= 18100:
        screen.fill((0, 0, 0))
        Awareness_text()        

    if paused:
        left_click = pygame.mouse.get_pressed()[0]
        RenderPausedMenu(screen, art)

        paused_text = get_font_BOLD(100).render("Paused", True, ("#C0BEBE"))
        screen.blit(paused_text, (440, 14))

        Resume_text = get_font(100).render("RESUME", True, ("#C0BEBE"))
        resume_rect = Resume_text.get_rect(center=(665, 300))

        quit_text = get_font(100).render("QUIT", True, ("#C0BEBE"))
        quit_rect = quit_text.get_rect(center=(650, 550))

        if resume_rect.collidepoint(mouse_pos):
            Resume_text = get_font(100).render("RESUME", True, ("#FFFFFF"))
        elif quit_rect.collidepoint(mouse_pos):
            quit_text = get_font(100).render("QUIT", True, ("#FFFFFF"))

        screen.blit(Resume_text, resume_rect)
        screen.blit(quit_text, quit_rect)

        if resume_rect.collidepoint(mouse_pos) and left_click:
            paused = False

        elif quit_rect.collidepoint(mouse_pos) and left_click:
            main_menu()
            MenuTrack()
                
    if j1_trigger:
            screen.fill((0, 0, 0))
            move_left = False
            move_right = False
            current_frame_surface = jumpscare_1_data.get_frame(frame_j)
            screen.blit(current_frame_surface, (400, 0))
            if frame_j == jumpscare_1_data.total_frames - 1:
                j1_trigger = False

    if j2_trigger:
        screen.fill((0, 0, 0))
        move_left = False
        move_right = False
        current_frame_surface = jumpscare_2_data.get_frame(frame_j2)
        screen.blit(current_frame_surface, (400, 0))
        if frame_j2 == jumpscare_2_data.total_frames - 1:
            j2_trigger = False
            minigame_2.has_no_options = False
    
    surface1.fill("#7a4841")
    screen.blit(surface1, (surface1_rect.x - camera_x, surface1_rect.y))

    process = psutil.Process(os.getpid())
    print(f"RAM usage: {process.memory_info().rss / (1024 * 1024):.2f} MB")
    pygame.display.update()

pygame.quit()
sys.exit()