import pygame

class TransitionObj:
    def __init__(self, screen_size, SubtractingInt=20):
        self.width, self.height = screen_size
        self.SubtractingInt = SubtractingInt

        self.active = False
        self.val = 200
        self.Surface = pygame.Surface((0, 0, 0))
        self.Surface.fill((0, 0, 0))

    def start(self):
        self.active = True
        self.val = 200

    def update(self):
        if not self.active:
            return
        
        self.val -= self.SubtractingInt

        if self.val <= 0:
            self.val = 0
            self.active = False

    def draw(self, screen):
        if not self.active:
            return
        
        self.Surface.set_alpha(self.val)
        screen.blit(self.Surface, (0, 0))