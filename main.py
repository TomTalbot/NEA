import pygame
import random
import PyQt5
import menu



'''
initial ideas:
side scrolling 2 mario style platformer with procedural generation, obstacles and potentially enemies?
implementing PyQt5 as pygame menus are a ball-ache. First have pyqt5 for menu and what not, when ready the player
selects a play option which deinitialises the PyQt5 library and enables Pygame.
'''




pygame.init()

clock = pygame.time.Clock()
FPS = 60

FONT = pygame.font.SysFont('Times New Roman', 26)

RED = (255,0,0)

GREEN = (0,255,0)

BLUE = (0,0,255)

#Window
WIDTH = 600
HEIGHT = 400


WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Unraveling worlds - TBD")
