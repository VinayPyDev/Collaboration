import pygame

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class TransitionObj:
    def __init__(self, screen_size, SubtractingInt=200):
        self.width, self.height = screen_size
        self.SubtractingInt = SubtractingInt

        self.active = False
        self.val = 200
        self.Surface = pygame.Surface((self.width, self.height))
        self.Surface.fill((0, 0, 0))
        self.reverse = False
        self.wait_time = 0
        self.waiting = False

    def start(self, wait_duration=0, reverse=False):
        self.active = True
        self.val = 0 if not reverse else 255
        self.reverse = reverse
        self.wait_time = wait_duration
        self.waiting = False

    def update(self, dt):
            if not self.active:
                return
            
            if self.waiting:
                self.wait_time -= int(dt * 1000)
                if self.wait_time <= 0:
                    # Automatically start fading back out
                    self.reverse = True
                    self.waiting = False
                    self.wait_time = 0
                return
            
            if not self.reverse:
                self.val += 180 * dt
                if self.val >= 255:
                    self.val = 255
                    self.waiting = True
            else:
                self.val -= 180 * dt
                if self.val <= 0:
                    self.val = 0
                    self.active = False
    def draw(self, screen):
        if not self.active:
            return
        
        self.Surface.set_alpha(int(self.val))
        screen.blit(self.Surface, (0, 0))

fade = TransitionObj((WIDTH, HEIGHT))

def fadeout():
    fade_surface = pygame.Surface((WIDTH, HEIGHT)).convert()
    fade_surface.fill("black")
    for i in range(0, 256, 2):
        fade_surface.set_alpha(i)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)  

def fadein(new_level_surface):
    fade_surface = pygame.Surface((WIDTH, HEIGHT)).convert()
    fade_surface.fill("black")
    for i in range(0, 256, 2):
        screen.blit(new_level_surface, (0, 0))
        
        fade_surface.set_alpha(255 - i)
        screen.blit(fade_surface, (0, 0))
        
        pygame.display.update()
        pygame.time.delay(5)

alpha = 0
def FadeTextCalc(alpha, fading=True, speed=3):
    if fading:
        alpha += speed
        if alpha >= 255:
            alpha = 255
    else:
        alpha -= speed
        if alpha <= 0:
            alpha = 0
    return alpha

def FadeTextSurf(orig_surf, alpha):
    txt_surf = orig_surf.copy()
    alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
    alpha_surf.fill((255, 255, 255, int(alpha)))
    txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return txt_surf