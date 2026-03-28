import pygame

WIDTH = 1280
HEIGHT = 720

class TransitionObj:
    def __init__(self, screen_size, SubtractingInt=200):
        self.width, self.height = screen_size
        self.SubtractingInt = SubtractingInt

        self.active = False
        self.val = 200
        self.Surface = pygame.Surface((self.width, self.height))
        self.Surface.fill((0, 0, 0))

    def start(self):
        self.active = True
        self.val = 0

    def update(self, dt):
        if not self.active:
            return
        
        self.val += 51 * dt

        if self.val >= 255:
            self.val = 255
            self.active = False

    def draw(self, screen):
        if not self.active:
            return
        
        self.Surface.set_alpha(int(self.val))
        screen.blit(self.Surface, (0, 0))

fade = TransitionObj((WIDTH, HEIGHT))