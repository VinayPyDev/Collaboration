import pygame
import sys
import random

from font import get_font

pygame.init()

def game2():
    WIDTH = 1280
    HEIGHT = 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    rect_obj_1 = pygame.Rect(1100, 100, 100, 100)
    rect_obj_2 = pygame.Rect(1100, 250, 100, 100)
    rect_obj_3 = pygame.Rect(1100, 400, 100, 100)
    rect_obj_4 = pygame.Rect(1100, 550, 100, 100)

    rect_obj_broken_1 = pygame.Rect(100, 100, 100, 100)
    rect_obj_broken_2 = pygame.Rect(100, 250, 100, 100)
    rect_obj_broken_3 = pygame.Rect(100, 400, 100, 100)
    rect_obj_broken_4 = pygame.Rect(100, 550, 100, 100)

    qte_bar_red = pygame.Rect(400, 100, 100, 600)
    qte_bar_green = pygame.Rect(400, random.randint(100, 599), 100, 100)

    green_bar_speed = 700
    green_bar_direction = 1

    x = 500
    click_point = pygame.Rect(x, random.randint(150, 550), 50, 50)

    # boolean checkers
    has_clicked = False
    has_picked_up = False

    picked_itm_1 = False
    picked_itm_2 = False
    picked_itm_3 = False
    picked_itm_4 = False

    broken_itm_1 = False
    broken_itm_2 = False
    broken_itm_3 = False
    broken_itm_4 = False

    while True:
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000

        if not picked_itm_1:
            pygame.draw.rect(screen, "purple", rect_obj_1)
        if not picked_itm_2:
            pygame.draw.rect(screen, "purple", rect_obj_2)
        if not picked_itm_3:
            pygame.draw.rect(screen, "purple", rect_obj_3)
        if not picked_itm_4:
            pygame.draw.rect(screen, "purple", rect_obj_4)

        pygame.draw.rect(screen, "red", qte_bar_red)

        click_it_text = get_font(45).render("CLICK THE GREEN!", True, (255, 255, 255))

        if has_picked_up:
            pygame.draw.rect(screen, "green", qte_bar_green)
            pygame.draw.rect(screen, "white", click_point)  
            qte_bar_green.y += green_bar_speed * green_bar_direction * dt

            screen.blit(click_it_text, (300, 0))

            if qte_bar_green.top <= qte_bar_red.top:
                green_bar_direction = 1
            
            if qte_bar_green.bottom >= qte_bar_red.bottom:
                green_bar_direction = -1

        if picked_itm_1 and has_clicked:
            broken_itm_1 = True
        if picked_itm_2 and has_clicked:
            broken_itm_2 = True
        if picked_itm_3 and has_clicked:
            broken_itm_3 = True
        if picked_itm_4 and has_clicked:
            broken_itm_4 = True

        if broken_itm_1:
            pygame.draw.rect(screen, "blue", rect_obj_broken_1)
            has_clicked = False
        if broken_itm_2:
            pygame.draw.rect(screen, "blue", rect_obj_broken_2)
            has_clicked = False
        if broken_itm_3:
            pygame.draw.rect(screen, "blue", rect_obj_broken_3)
            has_clicked = False
        if broken_itm_4:
            pygame.draw.rect(screen, "blue", rect_obj_broken_4)
            has_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_obj_1.collidepoint(event.pos):
                        picked_itm_1 = True
                        has_picked_up = True
                    if rect_obj_2.collidepoint(event.pos):
                        picked_itm_2 = True                    
                        has_picked_up = True
                    if rect_obj_3.collidepoint(event.pos):
                        picked_itm_3 = True
                        has_picked_up = True
                    if rect_obj_4.collidepoint(event.pos):
                        picked_itm_4 = True
                        has_picked_up = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    if qte_bar_green.top <= click_point.centery <= qte_bar_green.bottom:
                        print("clicked")
                        has_picked_up = False
                        has_clicked = True

        if broken_itm_1 and broken_itm_2 and broken_itm_3 and broken_itm_4:
            return False

        pygame.display.update()
