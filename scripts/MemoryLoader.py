import pygame

class MemoryAnimationLoader:
    def __init__(self, mem_frames, render_func, trigger_x, cooldown=100):
        self.mem_frames = mem_frames
        self.render_func = render_func  
        self.trigger_x = trigger_x
        self.cooldown = cooldown

        self.triggered = False          
        self.frame = 0 
        self.last_upd = pygame.time.get_ticks()

    def update(self, current_time, player_x):
        if not self.triggered and player_x >= self.trigger_x:
            self.triggered = True

        if self.triggered:
            if current_time - self.last_upd >= self.cooldown:
                self.last_upd = current_time
                self.frame = (self.frame + 1) % len(self.mem_frames)

    def draw(self, screen, camera_x):
        if self.triggered:
            current_frame_data = self.mem_frames[self.frame]
            self.render_func(screen, current_frame_data, camera_x)