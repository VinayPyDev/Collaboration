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
    
    tile_size = 32
    game_map = load_map("TestData/map")

    player_sprite = pygame.transform.scale(pygame.image.load(resource_path("TestData/testcase.png")).convert_alpha(), (100, 100))
    player_x = 640
    player_y = 50 * tile_size
    player_rect = pygame.Rect(player_x, player_y, 100, 100)
    player_speed = 400

    wall1 = pygame.transform.scale(pygame.image.load(resource_path("TestData/tile1.png")).convert_alpha(), (64, 64))
    wall2 = pygame.transform.scale(pygame.image.load(resource_path("TestData/tile2.png")).convert_alpha(), (64, 64))

    while True:
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000

        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                draw_x = x * tile_size
                draw_y = y * tile_size - camera_y
                if tile == '0':
                    screen.blit(wall1, (draw_x, draw_y))
                    tile_rects.append(pygame.Rect(draw_x, draw_y, tile_size, tile_size))
                elif tile == '1':
                    screen.blit(wall2, (draw_x, draw_y))
                    tile_rects.append(pygame.Rect(draw_x, draw_y, tile_size, tile_size))
                x += 1
            y += 1

        # print(player_rect.y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        camera_y = player_rect.centery - HEIGHT // 2
        print(player_rect.y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_rect.y -= player_speed * dt      
        if keys[pygame.K_s]:
            player_rect.y += player_speed * dt

        for tile_rect in tile_rects:
            if player_rect.colliderect(tile_rect):
                if keys[pygame.K_s]:
                    player_rect.bottom = tile_rect.top
                if keys[pygame.K_w]:
                    player_rect.top = tile_rect.bottom

        screen.blit(player_sprite, (player_rect.x, player_rect.y - camera_y))

        pygame.display.update()
    
game3()