import pygame
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

class M1Animations:
    def __init__(self, path, frames, width, height, scale, x_off, y_off, color):
        self.sheet = pygame.image.load(resource_path(path)).convert_alpha()
        self.total_frames = frames
        self.width = width
        self.height = height
        self.scale = scale
        self.x_off = x_off
        self.y_off = y_off
        self.color = color

    def get_frame(self, frame_index):
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA).convert_alpha() 
        image.blit(self.sheet, (0, 0), (frame_index * self.width, 0, self.width, self.height))
        image = pygame.transform.scale(image, (int(self.width * self.scale), int(self.height * self.scale)))
        image.set_colorkey(self.color)
        return image

    def draw(self, surface, frame_index, x, y, camera_x, camera_y):
        frame = self.get_frame(frame_index)
        draw_x = x - camera_x - self.x_off
        draw_y = y - camera_y - self.y_off
        surface.blit(frame, (draw_x, draw_y))

player_down_data = M1Animations(r"data2\player_down.png", 3, 48, 100, 3.125, 100, 100, (255, 255, 255))
player_right_data = M1Animations(r"data2\player_right.png", 3, 48, 100, 3.125, 100, 100, (255, 255, 255))
player_left_data = M1Animations(r"data2\player_left.png", 3, 48, 100, 3.125, 100, 100, (255, 255, 255))
player_up_data = M1Animations(r"data2\player_up.png", 3, 48, 100, 3.125, 100, 100, (255, 255, 255))

dog_idle_data = M1Animations(r"data2\dog_idle.png", 2, 48, 100, 3.125, 100, 100, (255, 255, 255))