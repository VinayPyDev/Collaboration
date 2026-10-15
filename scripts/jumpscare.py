import pygame
import sys
import os 

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

class JumpscarePlayer:
    def __init__(self, path, frames, width, height, scale, color):
        self.sheet = pygame.image.load(resource_path(path)).convert_alpha()
        self.total_frames = frames
        self.width = width
        self.height = height
        self.scale = scale
        self.color = color

    def get_frame(self, frame_index):
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame_index * self.width, 0, self.width, self.height))
        image = pygame.transform.scale(image, (int(self.width * self.scale), int(self.height * self.scale)))
        image.set_colorkey(self.color)
        return image

jumpscare_1_data = JumpscarePlayer("jumpscares/2ndJumpscareV2.png", 51, 150, 150, 4.5, (255, 255, 255))
jumpscare_2_data = JumpscarePlayer("jumpscares/LockerJumpscare.png", 32, 150, 150, 4.5, (0, 0, 255))