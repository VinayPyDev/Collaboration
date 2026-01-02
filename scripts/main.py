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

camera_x = 0

player_speed = 300
move_left = False
move_right = False

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

    if player.x - camera_x < -50:
        camera_x -= 100
        print("camera moved to left!")
    if player.x - camera_x > WIDTH - 125:
        camera_x += 100
        print("camera moved to right!")

    player.rect.topleft = (int(player.x - camera_x), int(player.y))
    
    screen.fill((30, 30, 30))
    screen.blit(player.image, player.rect)
    pygame.display.update()

pygame.quit()
sys.exit()