import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def SocialMediaButton():
    return {
        "youtube": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/youtube-scaled.png")).convert_alpha(), (150, 150)),
        "instagram": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/instagram-scaled.png")).convert_alpha(), (150, 150)),
        "facebook": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/facebook-scaled.png")).convert_alpha(), (150, 150)),
        "twitter": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/x-scaled.png")).convert_alpha(), (150, 150)),
        "itch.io": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/itch-scaled.png")).convert_alpha(), (150, 150)),
        "steam": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/steam-scaled.png")).convert_alpha(), (150, 150)),
        "tiktok": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/tiktok-scaled1.png")).convert_alpha(), (150, 150)),
        "twitch": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/twitch-scaled.png")).convert_alpha(), (150, 150))
    }

def SocialMediaButtonShrinked():
    return {
        "youtube_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/youtube-scaled.png")).convert_alpha(), (120, 120)),
        "instagram_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/instagram-scaled.png")).convert_alpha(), (120, 120)),
        "facebook_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/facebook-scaled.png")).convert_alpha(), (120, 120)),
        "twitter_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/x-scaled.png")).convert_alpha(), (120, 120)),
        "itch.io_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/itch-scaled.png")).convert_alpha(), (120, 120)),
        "steam_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/steam-scaled.png")).convert_alpha(), (120, 120)),
        "tiktok_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/tiktok-scaled1.png")).convert_alpha(), (120, 120)),
        "twitch_small": pygame.transform.scale(pygame.image.load(resource_path("data/social media sprites/twitch-scaled.png")).convert_alpha(), (120, 120))
    }

def RenderYoutubeButton(screen, art):
    screen.blit(art["youtube"], (0, 600))
def RenderInstagramButton(screen, art):
    screen.blit(art["instagram"], (150, 600))
def RenderFaceBookButton(screen, art):
    screen.blit(art["facebook"], (300, 600))
def RenderTwitterButton(screen, art):
    screen.blit(art["twitter"], (450, 600))
def RenderItchIoButton(screen, art):
    screen.blit(art["itch.io"], (600, 600))
def RenderSteamButton(screen, art):
    screen.blit(art["steam"], (750, 600))
def RenderTikTokButton(screen, art):
    screen.blit(art["tiktok"], (900, 600))
def RenderTwitch(screen, art):
    screen.blit(art["twitch"], (1050, 600))

def HoverBar():
    return {
        "if_hovered": pygame.transform.scale(pygame.image.load(resource_path("data/slider.png")).convert_alpha(), (500, 650))
    }
def RenderHoverBar(screen, art):
    screen.blit(art["if_hovered"], (0, 626 - 600))
def RenderHoverBar2(screen, art):
    screen.blit(art["if_hovered"], (150, 626 - 600))
def RenderHoverBar3(screen, art):
    screen.blit(art["if_hovered"], (300, 626 - 600))
def RenderHoverBar4(screen, art):
    screen.blit(art["if_hovered"], (450, 626 - 600))
def RenderHoverBar5(screen, art):
    screen.blit(art["if_hovered"], (600, 626 - 600))
def RenderHoverBar6(screen, art):
    screen.blit(art["if_hovered"], (750, 626 - 600))
def RenderHoverBar7(screen, art):
    screen.blit(art["if_hovered"], (850, 626 - 600))
def RenderHoverBar8(screen, art):
    screen.blit(art["if_hovered"], (875, 626 - 600))

# Done(TODO): animation of social media button
class ClickYoutube():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def RenderClickYoutube():
    youtube_spritesheet = pygame.image.load(resource_path("data/social media sprites/youtube-spritesheet.png")).convert_alpha()
    SpriteSheet = ClickYoutube(youtube_spritesheet)
    frames = 5
    width, height = 32, 32
    scale = 4.6875
    colorkey = (20, 20, 20)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class ClickInstagram():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def RenderClickInstagram():
    instagram_spritesheet = pygame.image.load(resource_path("data/social media sprites/instagram-spritesheet.png")).convert_alpha()
    SpriteSheet = ClickInstagram(instagram_spritesheet)
    frames = 5
    width, height = 32, 32
    scale = 4.6875
    colorkey = (20, 20, 20)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class ClickFacebook():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def RenderClickFacebook():
    facebook_spritesheet = pygame.image.load(resource_path("data/social media sprites/facebook-spritesheet.png")).convert_alpha()
    SpriteSheet = ClickFacebook(facebook_spritesheet)
    frames = 5
    width, height = 32, 32
    scale = 4.6875
    colorkey = (20, 20, 20)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class ClickTwitter():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def RenderClickTwitter():
    twitter_spritesheet = pygame.image.load(resource_path("data/social media sprites/x-spritesheet.png")).convert_alpha()
    SpriteSheet = ClickTwitter(twitter_spritesheet)
    frames = 5
    width, height = 32, 32
    scale = 4.6875
    colorkey = (20, 20, 20)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class ClickItchIo():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def RenderClickItchIo():
    itchio_spritesheet = pygame.image.load(resource_path("data/social media sprites/itch-spritesheet.png")).convert_alpha()
    SpriteSheet = ClickItchIo(itchio_spritesheet)
    frames = 5
    width, height = 32, 32
    scale = 4.6875
    colorkey = (20, 20, 20)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class ClickSteam():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def RenderClickSteam():
    steam_spritesheet = pygame.image.load(resource_path("data/social media sprites/steam-spritesheet.png")).convert_alpha()
    SpriteSheet = ClickSteam(steam_spritesheet)
    frames = 5
    width, height = 32, 32
    scale = 4.6875
    colorkey = (20, 20, 20)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class ClickTiktok():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def RenderClickTiktok():
    tiktok_spritesheet = pygame.image.load(resource_path("data/social media sprites/tiktok-spritesheet.png")).convert_alpha()
    SpriteSheet = ClickTiktok(tiktok_spritesheet)
    frames = 5
    width, height = 32, 32
    scale = 4.6875
    colorkey = (20, 20, 20)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

class ClickTwitch():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
def RenderClickTwitch():
    twitch_spritesheet = pygame.image.load(resource_path("data/social media sprites/twitch-spritesheet.png")).convert_alpha()
    SpriteSheet = ClickTwitch(twitch_spritesheet)
    frames = 5
    width, height = 32, 32
    scale = 4.6875
    colorkey = (20, 20, 20)

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey))

    return animation_list

# Animation Callouts
def LoadClickingYoutube(screen, image, pos):
    screen.blit(image, pos)
def LoadClickingInstagram(screen, image, pos):
    screen.blit(image, pos)
def LoadClickingFacebook(screen, image, pos):
    screen.blit(image, pos)
def LoadClickingTwitter(screen, image, pos):
    screen.blit(image, pos)
def LoadClickingItchIo(screen, image, pos):
    screen.blit(image, pos)
def LoadClickingSteam(screen, image, pos):
    screen.blit(image, pos)
def LoadClickingTiktok(screen, image, pos):
    screen.blit(image, pos)        
def LoadClickingTwitch(screen, image, pos):
    screen.blit(image, pos)