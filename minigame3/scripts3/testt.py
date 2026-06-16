import pygame
import sys
import os

pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def game3():       
    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
        
    camera_y = 0

    def load_map(path):
        with open(path + '.txt', 'r') as f:
            data = f.read().splitlines()
        return [list(row) for row in data]
    
    game_map = load_map("TestData/map")

    player_sprite = pygame.transform.scale(pygame.image.load(resource_path("TestData/testcase.png")).convert_alpha(), (100, 100))
    player_speed = 400

    wall1 = pygame.transform.scale(pygame.image.load(resource_path("TestData/tile1.png")).convert_alpha(), (64, 64))
    wall2 = pygame.transform.scale(pygame.image.load(resource_path("TestData/tile2.png")).convert_alpha(), (64, 64))

    tile_size = 32

    # 1. NEW: Calculate the map's total height and find the bottom-anchor starting Y
    total_map_height = len(game_map) * tile_size
    map_start_y = HEIGHT - total_map_height

    # 2. Spawn the player at the bottom of the map initially
    player_rect = pygame.Rect(640, HEIGHT - 150, 100, 100)

    while True:
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: player_rect.y -= player_speed * dt
        if keys[pygame.K_s]: player_rect.y += player_speed * dt
        if keys[pygame.K_a]: player_rect.x -= player_speed * dt        
        if keys[pygame.K_d]: player_rect.x += player_speed * dt

        # 3. Adjust camera_y relative to the bottom-anchored setup
        # Subtracting map_start_y keeps the camera matching our offset
        camera_y = (player_rect.centery - HEIGHT // 2) - map_start_y

        # Draw Map
        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                # 4. NEW: Factor map_start_y into the Y drawing position
                draw_x = x * tile_size
                draw_y = map_start_y + (y * tile_size) - camera_y

                if tile == '0':
                    screen.blit(wall1, (draw_x, draw_y))
                    tile_rects.append(pygame.Rect(draw_x, draw_y, tile_size, tile_size))
                elif tile == '1':
                    screen.blit(wall2, (draw_x, draw_y))
                    tile_rects.append(pygame.Rect(draw_x, draw_y, tile_size, tile_size))
                x += 1
            y += 1

        # 5. Draw Player: Apply the exact same Y shift
        screen.blit(player_sprite, (player_rect.x, player_rect.y - map_start_y - camera_y))

        pygame.display.update()

game3()