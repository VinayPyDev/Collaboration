import pygame

WIDTH = 1280
HEIGHT = 720

# class TransitionObj:
#     def __init__(self, screen_size, SubtractingInt=200):
#         self.width, self.height = screen_size
#         self.SubtractingInt = SubtractingInt

#         self.active = False
#         self.val = 200
#         self.Surface = pygame.Surface((self.width, self.height))
#         self.Surface.fill((0, 0, 0))
#         self.reverse = False

#     def start(self, reverse=False):
#         self.active = True
#         self.val = 0 if not reverse else 255
#         self.reverse = True

#     def update(self, dt):
#         if not self.active:
#             return
        
#         if not self.reverse:
#             self.val += 51 * dt
#             if self.val >= 255:
#                 self.val = 255
#                 self.active = False        
#         else:
#             self.val -= 51 * dt
#             if self.val <= 0:
#                 self.val = 0
#                 self.active = False

#     def draw(self, screen):
#         if not self.active:
#             return
        
#         self.Surface.set_alpha(int(self.val))
#         screen.blit(self.Surface, (0, 0))

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
                self.active = False
            return
        
        if not self.reverse:
            self.val += 51 * dt
            if self.val >= 255:
                self.val = 255
                self.waiting = True
        else:
            self.val -= 51 * dt
            if self.val <= 0:
                self.val = 0
                self.waiting = True

    def draw(self, screen):
        if not self.active:
            return
        
        self.Surface.set_alpha(int(self.val))
        screen.blit(self.Surface, (0, 0))

fade = TransitionObj((WIDTH, HEIGHT))