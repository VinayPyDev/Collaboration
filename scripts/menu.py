import pygame
import sys
import os
import webbrowser

from font import get_font, get_font_BOLD
from text import disclaimer_screen
from mediabutton import SocialMediaButton, SocialMediaButtonShrinked, HoverBar, RenderHoverBar, RenderHoverBar2, RenderHoverBar3, RenderHoverBar4
from mediabutton import RenderHoverBar5, RenderHoverBar6, RenderHoverBar7, RenderHoverBar8
from mediabutton import RenderClickYoutube, RenderClickInstagram, RenderClickTwitter, RenderClickFacebook, RenderClickItchIo, RenderClickTiktok, RenderClickSteam, RenderClickTwitch
from mediabutton import LoadClickingYoutube, LoadClickingInstagram, LoadClickingFacebook, LoadClickingTwitter, LoadClickingItchIo, LoadClickingSteam, LoadClickingTiktok, LoadClickingTwitch

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
art.update(SocialMediaButtonShrinked())
art.update(HoverBar())

masking_r = pygame.transform.scale(pygame.image.load(resource_path("data/masking_r.png")).convert_alpha(), (100, 100))
masking_l = pygame.transform.scale(pygame.image.load(resource_path("data/masking_l.png")).convert_alpha(), (100, 100))

design_1 = pygame.transform.scale(pygame.image.load(resource_path("data/mask1.png")).convert_alpha(), (170, 170))
design_2 = pygame.transform.scale(pygame.image.load(resource_path("data/mask2.png")).convert_alpha(), (170, 170))

youtube_frames = RenderClickYoutube()
instagram_frames = RenderClickInstagram()
facebook_frames = RenderClickFacebook()
twitter_frames = RenderClickTwitter()
itchio_frames = RenderClickItchIo()
steam_frames = RenderClickSteam()
tiktok_frames = RenderClickTiktok()
twitch_frames = RenderClickTwitch()

current_frame = 0
frame_timer = 0
frame_cooldown = 50

current_frame_idx1 = youtube_frames[0]
current_frame_idx2 = instagram_frames[0]
current_frame_idx3 = facebook_frames[0]
current_frame_idx4 = twitter_frames[0]
current_frame_idx5 = itchio_frames[0]
current_frame_idx6 = steam_frames[0]
current_frame_idx7 = tiktok_frames[0]
current_frame_idx8 = twitch_frames[0]

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
        
        if on_youtube_button:
            current_time = pygame.time.get_ticks()
            if current_frame < 4 and current_time - frame_timer > frame_cooldown:
                current_frame += 1
                frame_timer = current_time
            
            LoadClickingYoutube(screen, youtube_frames[current_frame], (0, 600))
        if on_instagram_button:
            current_time = pygame.time.get_ticks()
            if current_frame < 4 and current_time - frame_timer > frame_cooldown:
                current_frame += 1
                frame_timer = current_time
            
            LoadClickingInstagram(screen, instagram_frames[current_frame], (0, 600))
        if on_facebook_button:
            current_time = pygame.time.get_ticks()
            if current_frame < 4 and current_time - frame_timer > frame_cooldown:
                current_frame += 1
                frame_timer = current_time
            
            LoadClickingFacebook(screen, facebook_frames[current_frame], (0, 600))
        if on_twitter_button:
            current_time = pygame.time.get_ticks()
            if current_frame < 4 and current_time - frame_timer > frame_cooldown:
                current_frame += 1
                frame_timer = current_time
            
            LoadClickingTwitter(screen, twitter_frames[current_frame], (0, 600))
        if on_itchio_button:
            current_time = pygame.time.get_ticks()
            if current_frame < 4 and current_time - frame_timer > frame_cooldown:
                current_frame += 1
                frame_timer = current_time
            
            LoadClickingItchIo(screen, itchio_frames[current_frame], (0, 600))
        if on_tiktok_button:
            current_time = pygame.time.get_ticks()
            if current_frame < 4 and current_time - frame_timer > frame_cooldown:
                current_frame += 1
                frame_timer = current_time
            
            LoadClickingTiktok(screen, tiktok_frames[current_frame], (0, 600))
        if on_twitch_button:
            current_time = pygame.time.get_ticks()
            if current_frame < 4 and current_time - frame_timer > frame_cooldown:
                current_frame += 1
                frame_timer = current_time
            
            LoadClickingTwitch(screen, twitch_frames[current_frame], (0, 600))

        # Social media button
        youtube_btn_rect = art["youtube"].get_rect(topleft=(0, 600))
        instagram_btn_rect = art["instagram"].get_rect(topleft=(150, 600))
        facebook_btn_rect = art["facebook"].get_rect(topleft=(300, 600))
        twitter_btn_rect = art["twitter"].get_rect(topleft=(450, 600))
        itchio_btn_rect = art["itch.io"].get_rect(topleft=(600, 600))
        steam_btn_rect = art["steam"].get_rect(topleft=(750, 600))
        tiktok_btn_rect = art["tiktok"].get_rect(topleft=(900, 600))
        twitch_btn_rect = art["twitch"].get_rect(topleft=(1050, 600))

        #smaller rects
            # youtube
        youtube1_rect = art["youtube_small"].get_rect(topleft=(25, 60))
        youtube2_rect = art["youtube_small"].get_rect(topleft=(25, 140))
        youtube3_rect = art["youtube_small"].get_rect(topleft=(25, 220))
        youtube4_rect = art["youtube_small"].get_rect(topleft=(25, 300))
        youtube5_rect = art["youtube_small"].get_rect(topleft=(25, 380))
        youtube6_rect = art["youtube_small"].get_rect(topleft=(25, 460))
        youtube7_rect = art["youtube_small"].get_rect(topleft=(25, 540))
            # instagram
        instagram1_rect = art["instagram_small"].get_rect(topleft=(175, 60))
        instagram2_rect = art["instagram_small"].get_rect(topleft=(175, 140))
        instagram3_rect = art["instagram_small"].get_rect(topleft=(175, 220))
        instagram4_rect = art["instagram_small"].get_rect(topleft=(175, 300))
        instagram5_rect = art["instagram_small"].get_rect(topleft=(175, 380))
        instagram6_rect = art["instagram_small"].get_rect(topleft=(175, 460))
        instagram7_rect = art["instagram_small"].get_rect(topleft=(175, 540))

            # facebook
        facebook1_rect = art["facebook_small"].get_rect(topleft=(325, 60))
        facebook2_rect = art["facebook_small"].get_rect(topleft=(325, 140))
        facebook3_rect = art["facebook_small"].get_rect(topleft=(325, 220))
        facebook4_rect = art["facebook_small"].get_rect(topleft=(325, 300))
        facebook5_rect = art["facebook_small"].get_rect(topleft=(325, 380))
        facebook6_rect = art["facebook_small"].get_rect(topleft=(325, 460))
        facebook7_rect = art["facebook_small"].get_rect(topleft=(325, 540))

            # twitter
        twitter1_rect = art["twitter_small"].get_rect(topleft=(475, 60))
        twitter2_rect = art["twitter_small"].get_rect(topleft=(475, 140))
        twitter3_rect = art["twitter_small"].get_rect(topleft=(475, 220))
        twitter4_rect = art["twitter_small"].get_rect(topleft=(475, 300))
        twitter5_rect = art["twitter_small"].get_rect(topleft=(475, 380))
        twitter6_rect = art["twitter_small"].get_rect(topleft=(475, 460))
        twitter7_rect = art["twitter_small"].get_rect(topleft=(475, 540))

            # itch.io
        itchio1_rect = art["itch.io_small"].get_rect(topleft=(625, 60))
        itchio2_rect = art["itch.io_small"].get_rect(topleft=(625, 140))
        itchio3_rect = art["itch.io_small"].get_rect(topleft=(625, 220))
        itchio4_rect = art["itch.io_small"].get_rect(topleft=(625, 300))
        itchio5_rect = art["itch.io_small"].get_rect(topleft=(625, 380))
        itchio6_rect = art["itch.io_small"].get_rect(topleft=(625, 460))
        itchio7_rect = art["itch.io_small"].get_rect(topleft=(625, 540))

            # steam
        steam1_rect = art["steam_small"].get_rect(topleft=(775, 60))
        steam2_rect = art["steam_small"].get_rect(topleft=(775, 140))
        steam3_rect = art["steam_small"].get_rect(topleft=(775, 220))
        steam4_rect = art["steam_small"].get_rect(topleft=(775, 300))
        steam5_rect = art["steam_small"].get_rect(topleft=(775, 380))
        steam6_rect = art["steam_small"].get_rect(topleft=(775, 460))
        steam7_rect = art["steam_small"].get_rect(topleft=(775, 540))

            # tiktok
        tiktok1_rect = art["tiktok_small"].get_rect(topleft=(875, 60))
        tiktok2_rect = art["tiktok_small"].get_rect(topleft=(875, 140))
        tiktok3_rect = art["tiktok_small"].get_rect(topleft=(875, 220))
        tiktok4_rect = art["tiktok_small"].get_rect(topleft=(875, 300))
        tiktok5_rect = art["tiktok_small"].get_rect(topleft=(875, 380))
        tiktok6_rect = art["tiktok_small"].get_rect(topleft=(875, 460))
        tiktok7_rect = art["tiktok_small"].get_rect(topleft=(875, 540))
            
            # twitch
        twitch1_rect = art["twitch_small"].get_rect(topleft=(900, 60))
        twitch2_rect = art["twitch_small"].get_rect(topleft=(900, 140))
        twitch3_rect = art["twitch_small"].get_rect(topleft=(900, 220))
        twitch4_rect = art["twitch_small"].get_rect(topleft=(900, 300))
        twitch5_rect = art["twitch_small"].get_rect(topleft=(900, 380))
        twitch6_rect = art["twitch_small"].get_rect(topleft=(900, 460))
        twitch7_rect = art["twitch_small"].get_rect(topleft=(900, 540))

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
            screen.blit(art["youtube_small"], youtube1_rect)
            screen.blit(art["youtube_small"], youtube2_rect)
            screen.blit(art["youtube_small"], youtube3_rect)
            screen.blit(art["youtube_small"], youtube4_rect)
            screen.blit(art["youtube_small"], youtube5_rect)
            screen.blit(art["youtube_small"], youtube6_rect)
            screen.blit(art["youtube_small"], youtube7_rect)

            text1_Utube = get_font(48).render("VinayPyDev", True, (0, 0, 0))
            screen.blit(text1_Utube, (150, 100))
            text2_Utube = get_font(48).render("LucaArt", True, (0, 0, 0))
            screen.blit(text2_Utube, (150, 180))
            text3_Utube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text3_Utube, (130, 260))
            text4_Utube = get_font(48).render("Toasty", True, (0, 0, 0))
            screen.blit(text4_Utube, (150, 340))
            text5_Utube = get_font(48).render("Kaan", True, (0, 0, 0))
            screen.blit(text5_Utube, (150, 420))
            text6_Utube = get_font(48).render("DVD", True, (0, 0, 0))
            screen.blit(text6_Utube, (150, 500))

        if on_instagram_button:
            RenderHoverBar2(screen, art)
            screen.blit(art["instagram_small"], instagram1_rect)
            screen.blit(art["instagram_small"], instagram2_rect)
            screen.blit(art["instagram_small"], instagram3_rect)
            screen.blit(art["instagram_small"], instagram4_rect)
            screen.blit(art["instagram_small"], instagram5_rect)
            screen.blit(art["instagram_small"], instagram6_rect)
            screen.blit(art["instagram_small"], instagram7_rect)

            text1_Itube = get_font(48).render("VinayPyDev", True, (0, 0, 0))
            screen.blit(text1_Itube, (300, 100))
            text2_Itube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text2_Itube, (300, 180))
            text3_Itube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text3_Itube, (300, 260))
            text4_Itube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text4_Itube, (300, 340))
            text5_Itube = get_font(48).render("Kaan", True, (0, 0, 0))
            screen.blit(text5_Itube, (300, 420))
            text6_Itube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text6_Itube, (300, 500))

        if on_facebook_button:
            RenderHoverBar3(screen, art)
            screen.blit(art["facebook_small"], facebook1_rect)
            screen.blit(art["facebook_small"], facebook2_rect)
            screen.blit(art["facebook_small"], facebook3_rect)
            screen.blit(art["facebook_small"], facebook4_rect)
            screen.blit(art["facebook_small"], facebook5_rect)
            screen.blit(art["facebook_small"], facebook6_rect)
            screen.blit(art["facebook_small"], facebook7_rect)

            text1_Ftube = get_font(48).render("VinayPyDev", True, (0, 0, 0))
            screen.blit(text1_Ftube, (450, 100))
            text2_Ftube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text2_Ftube, (450, 180))
            text3_Ftube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text3_Ftube, (450, 260))
            text4_Ftube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text4_Ftube, (450, 340))
            text5_Ftube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text5_Ftube, (450, 420))
            text6_Ftube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text6_Ftube, (450, 500))

        if on_twitter_button:
            RenderHoverBar4(screen, art)
            screen.blit(art["twitter_small"], twitter1_rect)
            screen.blit(art["twitter_small"], twitter2_rect)
            screen.blit(art["twitter_small"], twitter3_rect)
            screen.blit(art["twitter_small"], twitter4_rect)
            screen.blit(art["twitter_small"], twitter5_rect)
            screen.blit(art["twitter_small"], twitter6_rect)
            screen.blit(art["twitter_small"], twitter7_rect)

            text1_Ttube = get_font(48).render("VinayPyDev", True, (0, 0, 0))
            screen.blit(text1_Ttube, (600, 100))
            text2_Ttube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text2_Ttube, (600, 180))
            text3_Ttube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text3_Ttube, (600, 260))
            text4_Ttube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text4_Ttube, (600, 340))
            text5_Ttube = get_font(48).render("Kaan", True, (0, 0, 0))
            screen.blit(text5_Ttube, (600, 420))
            text6_Ttube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text6_Ttube, (600, 500))

        if on_itchio_button:
            RenderHoverBar5(screen, art)
            screen.blit(art["itch.io_small"], itchio1_rect)
            screen.blit(art["itch.io_small"], itchio2_rect)
            screen.blit(art["itch.io_small"], itchio3_rect)
            screen.blit(art["itch.io_small"], itchio4_rect)
            screen.blit(art["itch.io_small"], itchio5_rect)
            screen.blit(art["itch.io_small"], itchio6_rect)
            screen.blit(art["itch.io_small"], itchio7_rect)

            text1_ITtube = get_font(48).render("VinayPyDev", True, (0, 0, 0))
            screen.blit(text1_ITtube, (750, 100))
            text2_ITtube = get_font(48).render("LucaArt", True, (0, 0, 0))
            screen.blit(text2_ITtube, (750, 180))
            text3_ITtube = get_font(48).render("Rusty9q1", True, (0, 0, 0))
            screen.blit(text3_ITtube, (750, 260))
            text4_ITtube = get_font(48).render("Toasty", True, (0, 0, 0))
            screen.blit(text4_ITtube, (750, 340))
            text5_ITtube = get_font(48).render("Kaan", True, (0, 0, 0))
            screen.blit(text5_ITtube, (750, 420))
            text6_ITtube = get_font(48).render("DVD", True, (0, 0, 0))
            screen.blit(text6_ITtube, (750, 500))

        if on_steam_button:
            RenderHoverBar6(screen, art)
            screen.blit(art["steam_small"], steam1_rect)
            screen.blit(art["steam_small"], steam2_rect)
            screen.blit(art["steam_small"], steam3_rect)
            screen.blit(art["steam_small"], steam4_rect)
            screen.blit(art["steam_small"], steam5_rect)
            screen.blit(art["steam_small"], steam6_rect)
            screen.blit(art["steam_small"], steam7_rect)

            text1_Stube = get_font(48).render("VinayPyDev", True, (0, 0, 0))
            screen.blit(text1_Stube, (900, 100))
            text2_Stube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text2_Stube, (900, 180))
            text3_Stube = get_font(48).render("Rusty9q1", True, (0, 0, 0))
            screen.blit(text3_Stube, (900, 260))
            text4_Stube = get_font(48).render("Toasty", True, (0, 0, 0))
            screen.blit(text4_Stube, (900, 340))
            text5_Stube = get_font(48).render("Kaan", True, (0, 0, 0))
            screen.blit(text5_Stube, (900, 420))
            text6_Stube = get_font(48).render("DVD", True, (0, 0, 0))
            screen.blit(text6_Stube, (900, 500))

        if on_tiktok_button:
            RenderHoverBar7(screen, art)
            screen.blit(art["tiktok_small"], tiktok1_rect)
            screen.blit(art["tiktok_small"], tiktok2_rect)
            screen.blit(art["tiktok_small"], tiktok3_rect)
            screen.blit(art["tiktok_small"], tiktok4_rect)
            screen.blit(art["tiktok_small"], tiktok5_rect)
            screen.blit(art["tiktok_small"], tiktok6_rect)
            screen.blit(art["tiktok_small"], tiktok7_rect)

            text1_TTtube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text1_TTtube, (980, 100))
            text2_TTtube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text2_TTtube, (980, 180))
            text3_TTtube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text3_TTtube, (980, 260))
            text4_TTtube = get_font(48).render("Toasty", True, (0, 0, 0))
            screen.blit(text4_TTtube, (980, 340))
            text5_TTtube = get_font(48).render("Kaan", True, (0, 0, 0))
            screen.blit(text5_TTtube, (1000, 420))
            text6_TTtube = get_font(48).render("Error 404", True, (0, 0, 0))
            screen.blit(text6_TTtube, (980, 500))

        if on_twitch_button:
            RenderHoverBar8(screen, art)
            screen.blit(art["twitch_small"], twitch1_rect)
            screen.blit(art["twitch_small"], twitch2_rect)
            screen.blit(art["twitch_small"], twitch3_rect)
            screen.blit(art["twitch_small"], twitch4_rect)
            screen.blit(art["twitch_small"], twitch5_rect)
            screen.blit(art["twitch_small"], twitch6_rect)
            screen.blit(art["twitch_small"], twitch7_rect)

            text1_TWtube = get_font(48).render("VinayPyDev", True, (0, 0, 0))
            screen.blit(text1_TWtube, (1000, 100))
            text2_TWtube = get_font(48).render("LucaArt", True, (0, 0, 0))
            screen.blit(text2_TWtube, (1000, 180))
            text3_TWtube = get_font(48).render("Rusty9q1", True, (0, 0, 0))
            screen.blit(text3_TWtube, (1000, 260))
            text4_TWtube = get_font(48).render("Toasty", True, (0, 0, 0))
            screen.blit(text4_TWtube, (1000, 340))
            text5_TWtube = get_font(48).render("Kaan", True, (0, 0, 0))
            screen.blit(text5_TWtube, (1000, 420))
            text6_TWtube = get_font(48).render("DVD", True, (0, 0, 0))
            screen.blit(text6_TWtube, (1000, 500))

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

            # print(mouse_pos)

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

                if event.button == 1:
                    if on_youtube_button:
                        if youtube1_rect.collidepoint(event.pos):
                            webbrowser.open("https://www.youtube.com/@VinayPyDev")
                        elif youtube2_rect.collidepoint(event.pos):
                            webbrowser.open("https://www.youtube.com/@LucaDoesTheArtThing")
                        elif youtube3_rect.collidepoint(event.pos):
                            print("BINGO2")
                        elif youtube4_rect.collidepoint(event.pos):
                            webbrowser.open("https://youtube.com/@tw0astey1?si=lEj-1kOZU8i90aj3")
                        elif youtube5_rect.collidepoint(event.pos):
                            webbrowser.open("https://www.youtube.com/@kaan_tuna")
                        elif youtube6_rect.collidepoint(event.pos):
                            print("BINGO6")
                        elif youtube7_rect.collidepoint(event.pos):
                            print("BINGO7")
                    if on_instagram_button:
                        if instagram1_rect.collidepoint(event.pos):
                            webbrowser.open("https://www.instagram.com/vinaypydev?igsh=djgxb2J2ZTU2bTh6")
                        elif instagram2_rect.collidepoint(event.pos):
                            print("BINGO1")
                        elif instagram3_rect.collidepoint(event.pos):
                            print("BINGO2")
                        elif instagram4_rect.collidepoint(event.pos):
                            print("BINGO4")
                        elif instagram5_rect.collidepoint(event.pos):
                            print("BINGO5")
                        elif instagram6_rect.collidepoint(event.pos):
                            print("BINGO6")
                        elif instagram7_rect.collidepoint(event.pos):
                            print("BINGO7")
                    if on_facebook_button:
                        if facebook1_rect.collidepoint(event.pos):
                            webbrowser.open("https://www.facebook.com/share/v/1DSGsez4rM/")
                        elif facebook2_rect.collidepoint(event.pos):
                            print("BINGO1")
                        elif facebook3_rect.collidepoint(event.pos):
                            print("BINGO2")
                        elif facebook4_rect.collidepoint(event.pos):
                            print("BINGO4")
                        elif facebook5_rect.collidepoint(event.pos):
                            print("BINGO5")
                        elif facebook6_rect.collidepoint(event.pos):
                            print("BINGO6")
                        elif facebook7_rect.collidepoint(event.pos):
                            print("BINGO7")
                    if on_twitter_button:
                        if twitter1_rect.collidepoint(event.pos):
                            webbrowser.open("https://www.twitter.com/VinayPyDev")
                        elif twitter2_rect.collidepoint(event.pos):
                            print("BINGO1")
                        elif twitter3_rect.collidepoint(event.pos):
                            print("BINGO2")
                        elif twitter4_rect.collidepoint(event.pos):
                            print("BINGO4")
                        elif twitter5_rect.collidepoint(event.pos):
                            webbrowser.open("https://www.twitter.com/plazmaero")
                        elif twitter6_rect.collidepoint(event.pos):
                            print("BINGO6")
                        elif twitter7_rect.collidepoint(event.pos):
                            print("BINGO7")
                    if on_itchio_button:
                        if itchio1_rect.collidepoint(event.pos):
                            webbrowser.open("https://VinayPyDev.itch.io")
                        elif itchio2_rect.collidepoint(event.pos):
                            webbrowser.open("https://that-guy-absorbed.itch.io")
                        elif itchio3_rect.collidepoint(event.pos):
                            webbrowser.open("https://Rusty9q1.itch.io")
                        elif itchio4_rect.collidepoint(event.pos):
                            webbrowser.open("https://elwario33.itch.io")
                        elif itchio5_rect.collidepoint(event.pos):
                            webbrowser.open("https://plazmaero.itch.io")
                        elif itchio6_rect.collidepoint(event.pos):
                            print("BINGO6")
                        elif itchio7_rect.collidepoint(event.pos):
                            print("BINGO7")
                    if on_steam_button:
                        if steam1_rect.collidepoint(event.pos):
                            webbrowser.open("https://www.steamcommunity.com/profiles/76561198697457955/")
                        elif steam2_rect.collidepoint(event.pos):
                            print("BINGO1")
                        elif steam3_rect.collidepoint(event.pos):
                            webbrowser.open("https://steamcommmunity.com/profiles/76561199507093252/")
                        elif steam4_rect.collidepoint(event.pos):
                            webbrowser.open("https://steamcommunity.com/profiles/76561199046217834/")
                        elif steam5_rect.collidepoint(event.pos):
                            print("BINGO5")
                        elif steam6_rect.collidepoint(event.pos):
                            print("BINGO6")
                        elif steam7_rect.collidepoint(event.pos):
                            print("BINGO7")
                    if on_tiktok_button:
                        if tiktok2_rect.collidepoint(event.pos):
                            print("BINGO1")
                        elif tiktok3_rect.collidepoint(event.pos):
                            print("BINGO2")
                        elif tiktok4_rect.collidepoint(event.pos):
                            print("BINGO4")
                        elif tiktok5_rect.collidepoint(event.pos):
                            webbrowser.open("https://www.tiktok.com/@plazmaero?lang=nl-NL")
                        elif tiktok6_rect.collidepoint(event.pos):
                            print("BINGO6")
                        elif tiktok7_rect.collidepoint(event.pos):
                            print("BINGO7")
                    if on_twitch_button:
                        if twitch1_rect.collidepoint(event.pos):
                            webbrowser.open("https://www.twitch.com/@VinayPyDev")
                        elif twitch2_rect.collidepoint(event.pos):
                            print("BINGO1")
                        elif twitch3_rect.collidepoint(event.pos):
                            print("BINGO2")
                        elif twitch4_rect.collidepoint(event.pos):
                            print("BINGO4")
                        elif twitch5_rect.collidepoint(event.pos):
                            print("BINGO5")
                        elif twitch6_rect.collidepoint(event.pos):
                            print("BINGO6")
                        elif twitch7_rect.collidepoint(event.pos):
                            print("BINGO7")

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