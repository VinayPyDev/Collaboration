import pygame
import sys
import os

# [Function imports]
from art import load_sunset_bg_full, load_dungeon_bg_full, load_sunset_bg_2_full, load_sunset_extra, load_keys, load_void_bg_full
from art import RenderPlayerIdleLeft, RenderPlayerIdleRight, RenderPlayerMoveLeft, RenderPlayerMoveRight
from art import Transition_backgrounds, LoadPage, LoadCollisionPage

from display import draw_sunset_bg_full, draw_dungeon_bg_full, draw_sunset_bg_2_full, render_memory_1, render_memory_2, render_memory_3, render_memory_4, render_memory_5, render_memory_6, render_memory_7, render_memory_8, render_memory_9
from display import draw_sunset_bg_extra_full, render_key1, render_key2, render_key3, render_key4, draw_dungeon_bg_full_2, draw_void_bg_full, draw_void_bg_2_full
from display import RenderSunsetToDungeon, RenderDungeonToVoid

from menu import main_menu
from memory_render import Render_memory_1, Render_memory_2, Render_memory_3, Render_memory_4, Render_memory_5, Render_memory_6, Render_memory_7, Render_memory_8, Render_memory_9
from transition import TransitionObj, fade
# from tilesets import Render_Sunrise_Tileset, Render_Dungeon_Tileset, Render_Void_Tileset
from tilesets import Load_Sunrise_Tileset, Load_Dungeon_Tileset, Load_Void_Tileset
from font import *
from text import Start_text

from key import RenderKeyA, RenderKeyS, RenderKeyD, RenderKeyW, LoadKeyA, LoadKeyD, LoadKeyS, LoadKeyW
from art import PauseImg, PauseMenu
from display import RenderPausedMenu

from music import MenuTrack

# Jumpscares
from jumpscare import Render_jumpscare_1, Render_jumpscare_2, LoadJumpscare1, LoadJumpscare2

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# minigames
from minigame1.scripts1.main import game1
from minigame2.scripts2.main import game2
from minigame3.scripts3.main import game3

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
dungeon_to_void = "The innocence has been stabbed and has turned"
dungeon_to_void_2 = " to the path of corruption"

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
KeyA = RenderKeyA()
frame_key_a = 0
last_update_key = pygame.time.get_ticks()
animation_cooldown_key = 150

KeyS = RenderKeyS()
frame_key_s = 0
last_update_key = pygame.time.get_ticks()
animation_cooldown_key = 150

KeyD = RenderKeyD()
frame_key_d = 0
last_update_key = pygame.time.get_ticks()
animation_cooldown_key = 150

KeyW = RenderKeyW()
frame_key_w = 0
last_update_key = pygame.time.get_ticks()
animation_cooldown_key = 150

key_pressed_a = False
key_pressed_s = False
key_pressed_d = False
key_pressed_w = False

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
map_end_x = 11000

text_displayed = False

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

            # if event.button == 1:
            #     print(mouse_pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main_menu()
            if event.key == pygame.K_e:
                if page_opened != 0:
                    page_opened = 0
                elif current_page != 0:
                    page_opened = current_page

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

    if key_pressed_s:
        pass

    if key_pressed_w:
        pass

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
                
    if current_time - last_update_key >= animation_cooldown_key:
        last_update_key = current_time

        if key_pressed_a:
            frame_key_a = (frame_key_a + 1) % len(KeyA)

        if key_pressed_s:
            frame_key_s = (frame_key_s + 1) % len(KeyS)

        if key_pressed_d:
            frame_key_d = (frame_key_d + 1) % len(KeyD)

        if key_pressed_w:
            frame_key_w = (frame_key_w + 1) % len(KeyW)

        if not key_pressed_a:
            frame_key_a = 0

        if not key_pressed_s:
            frame_key_s = 0

        if not key_pressed_d:
            frame_key_d = 0

        if not key_pressed_w:
            frame_key_w = 0
        
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
        game1(screen)
        player_x = player_x + 10
        minigame1_started = True

    if player_x >= 6000 and not minigame2_started:
        game2(screen)
        player_x = player_x + 10
        minigame2_started = True

    if player_x >= 8800 and not minigame3_started:
        game3(screen)
        player_x = player_x + 10
        minigame3_started = True

    if minigame1_started:
        move_right = False
        move_left = False
        # minigame1_started = False
    if minigame2_started:
        move_right = False
        move_left = False
        # minigame2_started = False
    if minigame3_started:
        move_right = False
        move_left = False

    if not j1_started and player_x > 10120:
        j1_trigger = True
        j1_started = True

    if not j2_started and player_x > 8000:
        j2_trigger = True
        j2_started = True

    if not memory1Trigger and player_x >= 1260:
        memory1Trigger = True
    if not memory2Trigger and player_x >= 3450:
        memory2Trigger = True
    if not memory3Trigger and player_x >= 4000:
        memory3Trigger = True
    if not memory4Trigger and player_x >= 5240:
        memory4Trigger = True
    if not memory5Trigger and player_x >= 6234:
        memory5Trigger = True
    if not memory6Trigger and player_x >= 7040:
        memory6Trigger = True
    if not memory7Trigger and player_x >= 8158:
        memory7Trigger = True
    if not memory8Trigger and player_x >= 9328:
        memory8Trigger = True 
    if not memory9Trigger and player_x >= 11750:
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
    
    if player_x >= 9700 and current_bg == "dungeon" and in_dungeon and not dungeon_fade_triggered:
        transition_text_surface = get_font_BOLD(45).render(dungeon_to_void, True, (244, 244, 244))
        transition_text_surface_2 = get_font_BOLD(45).render(dungeon_to_void_2, True, (244, 244, 244))
        text_timer = 4000
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

    render_key1(screen, art) 
    render_key2(screen, art)
    render_key3(screen, art)
    render_key4(screen, art)

    LoadKeyA(screen, KeyA[frame_key_a if key_pressed_a else 0], (10, 30))
    LoadKeyS(screen, KeyS[frame_key_s if key_pressed_s else 0], (77, 30))
    LoadKeyD(screen, KeyD[frame_key_d if key_pressed_d else 0], (140, 30))
    LoadKeyW(screen, KeyW[frame_key_w if key_pressed_w else 0], (75, -35))

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

    pygame.display.update()

pygame.quit()
sys.exit()