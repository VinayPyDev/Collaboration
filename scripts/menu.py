import pygame
import sys
import os

from font import get_font, get_font_BOLD
from text import disclaimer_screen
from mediabutton import SocialMediaButton, HoverBar, RenderHoverBar, RenderHoverBar2, RenderHoverBar3, RenderHoverBar4
from mediabutton import RenderHoverBar5, RenderHoverBar6, RenderHoverBar7, RenderHoverBar8

pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

art = {}
art.update(SocialMediaButton())
art.update(HoverBar())

masking_r = pygame.transform.scale(pygame.image.load(resource_path("data/masking_r.png")).convert_alpha(), (100, 100))
masking_l = pygame.transform.scale(pygame.image.load(resource_path("data/masking_l.png")).convert_alpha(), (100, 100))

design_1 = pygame.transform.scale(pygame.image.load(resource_path("data/mask1.png")).convert_alpha(), (170, 170))
design_2 = pygame.transform.scale(pygame.image.load(resource_path("data/mask2.png")).convert_alpha(), (170, 170))

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
        
        text = get_font_BOLD(45).render("Made by VinayPyDev, Lucas_art, Rusty9q1,", True, "White")
        rect = text.get_rect(center=(WIDTH // 2, 260))
        screen.blit(text, rect)
        
        text = get_font_BOLD(45).render("Toasty, Kaan, DVD,", True, "White")
        rect = text.get_rect(center=(WIDTH // 2, 460))
        screen.blit(text, rect)
        
        # text = get_font_BOLD(45).render("VinayPyDev, Lucas_art, Rusty9q1.", True, "White")
        # rect = text.get_rect(center=(WIDTH // 2, 260))
        # screen.blit(text, rect)

        back = BUTTON(None, (WIDTH // 2, 460), "BACK", get_font(75), "Green", "White")
        back.switch_color(mouse_pos)
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
    on_youtube_button = None
    on_instagram_button = None
    on_facebook_button = None
    on_twitter_button = None
    on_itchio_button = None
    on_tiktok_button = None
    on_steam_button = None
    on_twitch_button = None
    while True:
        screen.fill((0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(masking_r, (700, 200))
        screen.blit(masking_l, (475, 200))

        screen.blit(masking_r, (775, 350))
        screen.blit(masking_l, (400, 350))

        screen.blit(masking_r, (685, 500))
        screen.blit(masking_l, (475, 500))

        screen.blit(design_1, (WIDTH - 170, HEIGHT - 170))
        screen.blit(design_2, (0, HEIGHT - 170))

        title = get_font(80).render("Voices of Silent Shadows", True, "#BEBEBE")
        screen.blit(title, (80, 40))

        play = BUTTON(None, (640, 250), "PLAY", get_font(80), "#636363", "#FFFFFF")
        options_btn = BUTTON(None, (640, 400), "OPTIONS", get_font(80), "#636363", "#FFFFFF")
        quit_btn = BUTTON(None, (640, 550), "QUIT", get_font(80), "#636363", "#FFFFFF")

        for btn in [play, options_btn, quit_btn]:
            btn.switch_color(mouse_pos)
            btn.update()
        
        # Social media button
        youtube_btn_rect = art["youtube"].get_rect(topleft=(0, 570))
        instagram_btn_rect = art["instagram"].get_rect(topleft=(150, 570))
        facebook_btn_rect = art["facebook"].get_rect(topleft=(300, 570))
        twitter_btn_rect = art["twitter"].get_rect(topleft=(450, 570))
        itchio_btn_rect = art["itch.io"].get_rect(topleft=(600, 570))
        steam_btn_rect = art["steam"].get_rect(topleft=(750, 570))
        tiktok_btn_rect = art["tiktok"].get_rect(topleft=(900, 570))
        twitch_btn_rect = art["twitch"].get_rect(topleft=(1050, 570))

        screen.blit(art["youtube"], youtube_btn_rect)
        screen.blit(art["instagram"], instagram_btn_rect)
        screen.blit(art["facebook"], facebook_btn_rect)
        screen.blit(art["twitter"], twitter_btn_rect)
        screen.blit(art["itch.io"], itchio_btn_rect)
        screen.blit(art["steam"], steam_btn_rect)
        screen.blit(art["tiktok"], tiktok_btn_rect)
        screen.blit(art["twitch"], twitch_btn_rect)

        if on_youtube_button:
            RenderHoverBar(screen, art)
        if on_instagram_button:
            RenderHoverBar2(screen, art)
        if on_facebook_button:
            RenderHoverBar3(screen, art)
        if on_twitter_button:
            RenderHoverBar4(screen, art)
        if on_itchio_button:
            RenderHoverBar5(screen, art)
        if on_steam_button:
            RenderHoverBar6(screen, art)
        if on_tiktok_button:
            RenderHoverBar7(screen, art)
        if on_twitch_button:
            RenderHoverBar8(screen, art)

        if on_youtube_button is None:
            on_youtube_button = False
        if on_instagram_button is None:
            on_instagram_button = False
        if on_facebook_button is None:
            on_facebook_button = False
        if on_twitter_button is None:
            on_twitter_button = False
        if on_itchio_button is None:
            on_itchio_button = False
        if on_steam_button is None:
            on_steam_button = False
        if on_tiktok_button is None:
            on_tiktok_button = False
        if on_twitch_button is None:
            on_twitch_button = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if youtube_btn_rect.collidepoint(mouse_pos):
                    on_youtube_button = not on_youtube_button

                elif instagram_btn_rect.collidepoint(mouse_pos):
                    on_instagram_button = not on_instagram_button
                
                elif facebook_btn_rect.collidepoint(mouse_pos):
                    on_facebook_button = not on_facebook_button
                
                elif twitter_btn_rect.collidepoint(mouse_pos):
                    on_twitter_button = not on_twitter_button
                
                elif itchio_btn_rect.collidepoint(mouse_pos):
                    on_itchio_button = not on_itchio_button

                elif steam_btn_rect.collidepoint(mouse_pos):
                    on_steam_button = not on_steam_button

                elif tiktok_btn_rect.collidepoint(mouse_pos):
                    on_tiktok_button = not on_tiktok_button

                elif twitch_btn_rect.collidepoint(mouse_pos):
                    on_twitch_button = not on_twitch_button

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.check_input(mouse_pos):
                    pygame.time.wait(100)
                    disclaimer_screen()
                    return "PLAY"
                if options_btn.check_input(mouse_pos):
                    options()
                if quit_btn.check_input(mouse_pos):
                    pygame.time.wait(500)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()