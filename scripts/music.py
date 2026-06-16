import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

breathing_sound = pygame.mixer.load("music/Sounds and music/Breathing (1).mp3")
def Breathing():
    breathing_sound.play()

# Tracks
def Morning_track():
    pygame.mixer_music.load("music/Sounds and music/Morning dawn.mp3")
    pygame.mixer_music.set_volume(0.4)
    pygame.mixer_music.play()
def Morning_chirping():
    pygame.mixer_music.load("music/Sounds and music/Ambience .mp3")
    pygame.mixer_music.set_volume(0.6)
    pygame.mixer_music.play()

def Dungeon_track():
    pygame.mixer_music.load("music/Sounds and music/Police .mp3")
    pygame.mixer_music.set_volume(0.4)
    pygame.mixer_music.play()

# def 

def Void_track():
    pygame.mixer_music.load("music/Sounds and music/Hello.mp3")
    pygame.mixer_music.set_volume(0.4)
    pygame.mixer_music.play()
def Void_background_track():
    pygame.mixer_music.load("music/Sounds and music/Distraction.mp3")
    pygame.mixer_music.set_volume(0.4)
    pygame.mixer_music.play()

def Final_text():
    pygame.mixer_music.load("music/Sounds and music/Bully.mp3")
    pygame.mixer_music.set_volume(0.4)
    pygame.mixer_music.play()