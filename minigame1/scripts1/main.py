import pygame
import sys

from font import get_font

pygame.init()

def game1():
    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    camera_x = 0
    camera_y = 0

    rect = pygame.Rect(640, 360, 100, 100)
    speed = 100

    food_scored = 0
    water_scored = 0

    rect2 = pygame.Rect(100, 300, 64, 64)
    rect3 = pygame.Rect(400, 200, 64, 64)
    rect4 = pygame.Rect(700, 100, 64, 64)
    rect5 = pygame.Rect(500, 500, 64, 64)
    rect6 = pygame.Rect(1100, 600, 64, 64)

    dog_rect = pygame.Rect(800, 500, 100, 100)
    water_needs = 2
    food_needs = 3

    not_picked1 = True
    not_picked2 = True
    not_picked3 = True
    not_picked4 = True
    not_picked5 = True

    while True:
        dt = clock.tick(60) / 1000
        screen.fill((0, 0, 0))

        if not_picked1:
            pygame.draw.rect(screen, "blue", (rect2.x - camera_x, rect2.y - camera_y, rect2.width, rect2.height))
        if not_picked2:
            pygame.draw.rect(screen, "yellow", (rect3.x - camera_x, rect3.y - camera_y, rect3.width, rect3.height))
        if not_picked3:
            pygame.draw.rect(screen, "blue", (rect4.x - camera_x, rect4.y - camera_y, rect4.width, rect4.height))
        if not_picked4:
            pygame.draw.rect(screen, "yellow", (rect5.x - camera_x, rect5.y - camera_y, rect5.width, rect5.height))
        if not_picked5:
            pygame.draw.rect(screen, "blue", (rect6.x - camera_x, rect6.y - camera_y, rect6.width, rect6.height))

        pygame.draw.rect(screen, "green", (dog_rect.x - camera_x, dog_rect.y - camera_y, dog_rect.width, dog_rect.height))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and water_scored > 0:
                    water_scored -= 1
                    water_needs -= 1
                elif event.key == pygame.K_e and food_scored > 0:
                    food_scored -= 1
                    food_needs -= 1

        camera_x = rect.x - WIDTH // 2
        camera_y = rect.y - HEIGHT // 2
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_w:
            #         rect.y -= speed * dt
            #     if event.key == pygame.K_s:
            #         rect.y += speed * dt
            #     if event.key == pygame.K_a:
            #         rect.x -= speed * dt
            #     if event.key == pygame.K_d:
            #         rect.x += speed * dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            rect.x -= speed * dt
        if keys[pygame.K_d]:
            rect.x += speed * dt
        if keys[pygame.K_s]:
            rect.y += speed * dt
        if keys[pygame.K_w]:
            rect.y -= speed * dt

        if not_picked1 and rect.colliderect(rect2):
            not_picked1 = False
            food_scored = food_scored + 1
        if not_picked2 and rect.colliderect(rect3):
            not_picked2 = False
            water_scored = water_scored + 1
        if not_picked3 and rect.colliderect(rect4):
            not_picked3 = False
            food_scored = food_scored + 1
        if not_picked4 and rect.colliderect(rect5):
            not_picked4 = False
            water_scored = water_scored + 1
        if not_picked5 and rect.colliderect(rect6):
            not_picked5 = False
            food_scored = food_scored + 1        

        water_dog_needs = get_font(40).render(f"E to feed: {food_needs}", True, (255, 255, 255))
        food_dog_needs = get_font(40).render(f"F to water: {water_needs}", True, (255, 255, 255))

        if rect.colliderect(dog_rect):
            screen.blit(water_dog_needs, (700, 400))
            screen.blit(food_dog_needs, (700, 300))

            # if keys[pygame.K_f]:
            #     water_scored -= 1
            # elif keys[pygame.K_e]:
            #     food_scored -= 1

            if food_scored < 0:
                food_scored = 0
            elif water_scored < 0:
                water_scored = 0

            if food_needs < 0:
                food_needs = 0
            if water_needs < 0:
                water_needs = 0

        text1 = get_font(50).render(f"Food: {food_scored}", True, (255, 255, 255))
        text2 = get_font(50).render(f"Water: {water_scored}", True, (255, 255, 255))
        screen.blit(text1, (0, 0))
        screen.blit(text2, (0, 100))

        pygame.draw.rect(screen, (255, 0, 0), (rect.x - camera_x, rect.y - camera_y, rect.width, rect.height))
        
        pygame.display.update() 