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

def draw_sunset_bg_extra_full(screen, art, camera_x):
    screen.blit(art["sunset_ex"], (3000 - camera_x, -150))

def draw_sunset_bg_2_full(screen, art, camera_x):
    screen.blit(art["sunset_2"], (4000 - camera_x, -150))

def draw_dungeon_bg_full(screen, art, camera_x):
    screen.blit(art["dungeon"], (6000 - camera_x, -150))

def draw_dungeon_bg_full_2(screen, art, camera_x):
    screen.blit(art["dungeon"], (8932 - camera_x, -150))

# Memories
def render_memory_1(screen, frame_img, camera_x):
    screen.blit(frame_img, (2000 - camera_x, 200))

def render_memory_2(screen, frame_img, camera_x):
    screen.blit(frame_img, (3000 - camera_x, 200))

def render_memory_3(screen, frame_img, camera_x):
    screen.blit(frame_img, (7000 - camera_x, 200))

def render_memory_4(screen, frame_img, camera_x):
    screen.blit(frame_img, (8000 - camera_x, 200))

def render_memory_5(screen, frame_img, camera_x):
    screen.blit(frame_img, (10000 - camera_x, 200))

def render_memory_6(screen, frame_img, camera_x):
    screen.blit(frame_img, (12600 - camera_x, 200))

def render_memory_7(screen, frame_img, camera_x):
    screen.blit(frame_img, (14000 - camera_x, 200))

def render_memory_8(screen, frame_img, camera_x):
    screen.blit(frame_img, (16000 - camera_x, 200))

def render_memory_9(screen, frame_img, camera_x):
    screen.blit(frame_img, (18000 - camera_x, 200))

# Keys
def render_key1(screen, art, camera_x):
    screen.blit(art["key1"], (150 - camera_x, -150))
def render_key2(screen, art, camera_x):
    screen.blit(art["key2"], (50 - camera_x, -150))
def render_key3(screen, art, camera_x):
    screen.blit(art["key3"], (150 - camera_x, -150))
def render_key4(screen, art, camera_x):
    screen.blit(art["key4"], (200 - camera_x, -150))