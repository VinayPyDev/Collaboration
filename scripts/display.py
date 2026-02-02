def draw_player_idle(screen, art, x, y):
    img = art["idle_0"]
    rect = img.get_rect(center=(x, y))
    screen.blit(img, rect)

def draw_player_idle_left(screen, art, x, y):
    img = art["idle_1"]
    rect = img.get_rect(center=(x, y))
    screen.blit(img, rect)    

def draw_sunset_bg_full(screen, art, camera_x):
    screen.blit(art["sunset"], (-camera_x, -150))

def draw_sunset_bg_2_full(screen, art, camera_x):
    screen.blit(art["sunset_2"], (2900 - camera_x, -150))

def draw_dungeon_bg_full(screen, art, camera_x):
    screen.blit(art["dungeon"], (5800 - camera_x, -150))

# Memories
def render_memory_1(screen, frame_img, camera_x):
    screen.blit(frame_img, (1300 - camera_x, 300))

def render_memory_2(screen, frame_img, camera_x):
    screen.blit(frame_img, (2700 - camera_x, 300))

def render_memory_3(screen, frame_img, camera_x):
    screen.blit(frame_img, (4000 - camera_x, 300))
