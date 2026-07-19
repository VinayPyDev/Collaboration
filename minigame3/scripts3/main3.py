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

def get_font_BOLD(size):
    return pygame.font.Font(resource_path("font/PixeloidSans-Bold.ttf"), size)

def game3():       
    global get_font_BOLD

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

    jumpscare_img = pygame.transform.scale(pygame.image.load(resource_path("TestData/jumpscaer.png")).convert_alpha(), (1280, 720))

    player_sprite = pygame.transform.scale(pygame.image.load(resource_path("TestData/testcase.png")).convert_alpha(), (100, 100))
    player_x = 640
    player_y = 3000
    player_rect = pygame.Rect(player_x, player_y, 100, 100)
    player_speed = 0

    entity_rect = pygame.Rect(640, 4000, 100, 100)
    entity_speed = 340
    if_entity_near = False

    wall1 = pygame.transform.scale(pygame.image.load(resource_path("TestData/tile1.png")).convert_alpha(), (64, 64))
    wall2 = pygame.transform.scale(pygame.image.load(resource_path("TestData/tile2.png")).convert_alpha(), (64, 64))

    text = get_font_BOLD(80).render("RUN!!!", True, (255, 255, 255))

    while True:
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000

        entity_rect.y -= entity_speed * dt

        if entity_rect.y <= player_y + 350:
            if_entity_near = True
        if if_entity_near:
            player_speed = 340

        screen.blit(text, (500, 3300 - camera_y))

        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                world_x = x * tile_size
                world_y = y  * tile_size
                if tile == '0':
                    screen.blit(wall1, (world_x, world_y - camera_y))
                    tile_rects.append(pygame.Rect(world_x, world_y, tile_size, tile_size))
                elif tile == '1':
                    screen.blit(wall2, (world_x, world_y - camera_y))
                    tile_rects.append(pygame.Rect(world_x, world_y, tile_size, tile_size))
                x += 1
            y += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        camera_y = player_rect.centery - HEIGHT // 2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and if_entity_near:
            player_rect.y -= player_speed * dt      
        if keys[pygame.K_s] and if_entity_near:
            player_rect.y += player_speed * dt

        if player_rect.y >= 3073 and if_entity_near:
            player_rect.y = 3073

        screen.blit(player_sprite, (player_rect.x, player_rect.y - camera_y))
        pygame.draw.rect(screen, "black", (entity_rect.x, entity_rect.y - camera_y, entity_rect.width, entity_rect.height))
        
        if player_rect.y <= 55 and if_entity_near:
            player_speed = 0
        if player_rect.colliderect(entity_rect):
            entity_speed = 0
            player_speed = 0
            screen.blit(jumpscare_img, (0, 0))
            print("Get Jumpscared BOZO")
        
        pygame.display.update()
    
game3()