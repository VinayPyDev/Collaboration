import pygame

from font import get_font, get_font_BOLD

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def Disclaimer_text():
    header = get_font_BOLD(45).render("DISCLAIMER", True, "#FF0000")
    screen.blit(header, (500, 40))

    disclaimer_description = get_font(32).render("This game contains depictions of dark subject matter and mature them", True, "#DADADA") 
    disclaimer_description_miss = get_font(32).render("-es such as sucide, self harms and severe mental distress. Player", True, "#DADADA")
    disclaimer_description_2 = get_font(32).render("discretion is advised", True, "#DADADA")
    screen.blit(disclaimer_description, (0, 100))
    screen.blit(disclaimer_description_2, (0, 200))
    screen.blit(disclaimer_description_miss, (10, 150))

    age_restriction_note = get_font(32).render("Players below the age of 13 require parental supervision or ", True, "#DADADA")
    age_restriction_note_2 = get_font(32).render("guidance because of the mature content and themes", True, "#DADADA")
    screen.blit(age_restriction_note, (10, 300))
    screen.blit(age_restriction_note_2, (10, 360))

def Awareness_text():
    description = get_font(32).render("Thousands of lives of adolescents are lost due to bullying,", True, "#DADADA")
    description_2 = get_font(32).render("bullying isn't harmless but the emotional impact is chronic.", True, "#DADADA") 
    description_3 = get_font(32).render("Sometimes the limit is crossed to a point where sucidial thoughts begins rising until the life of the victim is over", True, "#DADADA")
    screen.blit(description, (0, 50))
    screen.blit(description_2, (0, 200))
    screen.blit(description_3, (0, 350))

def disclaimer_screen():
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    show_key = False
    running = True

    while running:
        screen.fill((10, 10, 10))

        Disclaimer_text()

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 5000:
            show_key = True

        if show_key:
            press_text = get_font_BOLD(45).render("Press any key to continue", True, "#FFFFFF")
            screen.blit(press_text, press_text.get_rect(center=(390, 650)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if show_key and event.type == pygame.KEYDOWN:
                running = False

        pygame.display.update()
        clock.tick(60)

def Start_text():
    text = get_font(45).render("Collect all the memories", True, "#000000")
    text_rect = text.rect(center=(200, -150))

    screen.blit(text, text_rect)
