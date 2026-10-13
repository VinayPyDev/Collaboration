import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 64)
orig_surf = font.render('enter the text', True, (255, 255, 255))
txt_surf = orig_surf.copy()

alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
alpha = 0

fade_dir = -1  # -1 means fading out, +1 means fading in

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    alpha += fade_dir * 3

    if alpha <= 0:
        alpha = 0
        fade_dir = 1   
    elif alpha >= 255:
        alpha = 255
        fade_dir = -1  

    txt_surf = orig_surf.copy()
    alpha_surf.fill((255, 255, 255, alpha))
    txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    screen.fill((30, 30, 30))
    screen.blit(txt_surf, (100, 150))
    pygame.display.flip()
    clock.tick(60)