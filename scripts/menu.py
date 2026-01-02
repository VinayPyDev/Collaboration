import pygame
import sys

from font import get_font

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class BUTTON:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, base_color)

        if self.image is None:
            self.image = self.text

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect) 

    def check_input(self, position):
        return self.rect.collidepoint(position)
    
    def switch_color(self, position):
        color = self.hovering_color if self.rect.collidepoint(position) else self.base_color
        self.text = self.font.render(self.text_input, True, color)

def options():
    while True:
        screen.fill("black")
        mouse_pos = pygame.mouse.get_pos()
        
        text = get_font(45).render("This is Made by VinayPyDev.", True, "White")
        rect = text.get_rect(center=(WIDTH // 2, 260))
        screen.blit(text, rect)

        back = BUTTON(None, (WIDTH // 2, 460), "BACK", get_font(75), "Green", "White")
        back.change_color(mouse_pos)
        back.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit( )
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.check_input(mouse_pos):
                    return

        pygame.display.update()

def main_menu():
    while True:
        screen.fill((40, 40, 40))
        mouse_pos = pygame.mouse.get_pos()

        title = get_font(85).render("Cards Of Soccer", True, "#0026FF")
        screen.blit(title, (40, 40))

        play = BUTTON(None, (165, 250), "PLAY", get_font(70), "#00B7FF", "White")
        options_btn = BUTTON(None, (240, 400), "OPTIONS", get_font(70), "#00B7FF", "White")
        quit_btn = BUTTON(None, (150, 550), "QUIT", get_font(70), "#00B7FF", "White")

        for btn in [play, options_btn, quit_btn]:
            btn.change_color(mouse_pos)
            btn.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.check_input(mouse_pos):
                    pygame.time.wait(100)
                    return "PLAY"
                if options_btn.check_input(mouse_pos):
                    options()
                if quit_btn.check_input(mouse_pos):
                    pygame.time.wait(500)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()