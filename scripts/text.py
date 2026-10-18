import pygame
import sys
import os

from art import LoadFlags
from font import get_font, get_font_BOLD
from thanks import ThanksToDevsScreen

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

art = {}
art.update(LoadFlags())

def Disclaimer_text():
    header = get_font_BOLD(45).render("DISCLAIMER", True, "#FF0000")
    screen.blit(header, (500, 40))

    disclaimer_description = get_font(32).render("This game contains depictions of dark subject matter and mature them", True, "#DADADA") 
    disclaimer_description_miss = get_font(32).render("-es such as sucide, self harms and severe mental distress. Player", True, "#DADADA")
    disclaimer_description_2 = get_font(32).render("discretion is advised", True, "#DADADA")
    screen.blit(disclaimer_description, (0, 100))
    screen.blit(disclaimer_description_2, (0, 200))
    screen.blit(disclaimer_description_miss, (10, 150))

    age_restriction_note = get_font(32).render("Players below the age of 16 require parental supervision or ", True, "#DADADA")
    age_restriction_note_2 = get_font(32).render("guidance because of the mature content and themes", True, "#DADADA")
    screen.blit(age_restriction_note, (10, 300))
    screen.blit(age_restriction_note_2, (10, 360))

def Awareness_text():
    global resource_path
    global get_font_BOLD
    description = get_font(32).render("Thousands of lives of adolescents are lost due to bullying,", True, "#DADADA")
    description_2 = get_font(32).render("bullying isn't harmless but the emotional impact is chronic.", True, "#DADADA") 
    description_3 = get_font(32).render("Sometimes the limit is crossed to a point where sucidial thoughts begins", True, "#DADADA")
    description_4 = get_font(32).render(" rising until the life of the victim is over", True, "#DADADA")
    screen.blit(description, (0, 25))
    screen.blit(description_2, (0, 100))
    screen.blit(description_3, (0, 175))
    screen.blit(description_4, (0, 250))

    screen.blit(art["Brazil"], (20, 320))
    screen.blit(art["France"], (20, 470))
    screen.blit(art["India"], (20, 620))
    screen.blit(art["Japan"], (625, 320))
    screen.blit(art["UK"], (625, 470))
    screen.blit(art["USA"], (625, 620))

    brazil_num = get_font_BOLD(45).render("+55 1131514109", True, "#FFFFFF")
    france_num = get_font_BOLD(45).render("+33 145394000", True, "#FFFFFF")
    india_num = get_font_BOLD(45).render("+91 8376804102", True, "#FFFFFF")
    japan_num = get_font_BOLD(45).render("+81 643954343", True, "#FFFFFF")    
    UK_num = get_font_BOLD(45).render("+44 8000684141", True, "#FFFFFF")
    USA_num = get_font_BOLD(45).render("988", True, "#FFFFFF")

    screen.blit(brazil_num, (130, 320))
    screen.blit(france_num, (130, 470))
    screen.blit(india_num, (130, 620))
    screen.blit(japan_num, (735, 320))
    screen.blit(UK_num, (735, 470))
    screen.blit(USA_num, (735, 620))

def disclaimer_screen():
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    show_key = False
    running = True

    while running:
        screen.fill((10, 10, 10))

        Disclaimer_text()

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:
            show_key = True

        if show_key:
            press_text = get_font_BOLD(45).render("Press E to continue", True, "#FFFFFF")
            screen.blit(press_text, press_text.get_rect(center=(390, 650)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if show_key and event.type == pygame.KEYDOWN:
                running = False

        pygame.display.flip()
        clock.tick(60)

def Start_text():
    text = get_font_BOLD(45).render("Collect all the memories", True, "#000000")
    text_rect = text.get_rect(center=(550, 35))

    screen.blit(text, text_rect)