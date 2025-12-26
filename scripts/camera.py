import pygame

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)

    def apply(self, entity):
        return entity.rect.move(-self.camera_rect.x, -self.camera_rect.y)

    def update(self, target):
        self.camera_rect.x = target.rect.centerx - self.camera_rect.w // 2
        self.camera_rect.y = target.rect.centery - self.camera_rect.h // 2
