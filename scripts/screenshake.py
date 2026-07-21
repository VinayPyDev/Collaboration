import random
import pygame

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 1. Create a dedicated game surface (buffer)
game_surface = pygame.Surface((WIDTH, HEIGHT))

# Shake variables
shake_timer = 0
shake_intensity = 0

running = True
while running:
    # Event tracking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Trigger shake on SPACEBAR press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shake_timer = 20  # Shake lasts for 20 frames
                shake_intensity = 8  # Shake up to 8 pixels max

    # 2. Draw everything to your game_surface (NOT screen)
    game_surface.fill((30, 30, 40))  # Dark background
    pygame.draw.rect(
        game_surface, (255, 100, 100), (WIDTH // 2 - 25, HEIGHT // 2 - 25, 50, 50)
    )

    # 3. Calculate screen shake offsets
    render_offset_x = 0
    render_offset_y = 0

    if shake_timer > 0:
        # Generate random offsets from -intensity to +intensity
        render_offset_x = random.randint(-shake_intensity, shake_intensity)
        render_offset_y = random.randint(-shake_intensity, shake_intensity)
        shake_timer -= 1  # Countdown timer

    # Clear main screen to hide edges during high-intensity shakes
    screen.fill((0, 0, 0))

    # 4. Blit the buffer to the screen with the calculated offset
    screen.blit(game_surface, (render_offset_x, render_offset_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
