import pygame
import sys
from art import load_player_idle
from camera import Camera

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

art = {}
art.update(load_player_idle())

class Player:
    def __init__(self, img, x, y):
        self.image = img
        self.rect = self.image.get_rect()
        self.x = float(x)
        self.y = float(y)
        self.rect.topleft = (self.x, self.y)

player = Player(art["idle_0"], 640, 360)
camera = Camera(WIDTH, HEIGHT)

player_speed = 300
move_left = False
move_right = False

WORLD_WIDTH = 4000
WORLD_HEIGHT = 1000

running = True
while running:
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
                running = False
                
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_LEFT):
                move_left = False
            if event.key in (pygame.K_d, pygame.K_RIGHT):
                move_right = False

    if move_left:
        player.x -= player_speed * dt
    if move_right:
        player.x += player_speed * dt

    player.x = max(0, min(player.x, WORLD_WIDTH - player.rect.width))
    player.rect.topleft = (int(player.x), int(player.y))

    camera.update(player)

    screen.fill((30, 30, 30))
    screen.blit(player.image, camera.apply(player))
    pygame.display.update()

pygame.quit()
sys.exit()
