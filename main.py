import pygame
import pygame_menu
import random
import PyQt5
import menu
import os
from sys import exit
from pygame import font
import button



'''
initial ideas:
side scrolling 2 mario style platformer with procedural generation, obstacles and potentially enemies?
implementing PyQt5 as pygame menus are a ball-ache. First have pyqt5 for menu and what not, when ready the player
selects a play option which deinitialises the PyQt5 library and enables Pygame.


dev log 1 8/9/22:
deciding to use pygame menus, due to the freedom and customisability - potentially?
'''

pygame.init()
pygame.mixer.init()


WIN = pygame.display.set_mode((400,400))
pygame.display.set_caption('Unraveling worlds?')

#game vars
game_paused = False


#font defining

FONT = pygame.font.SysFont('comicsans',40)

#colours
TEXT_COL = (255,255,255)


def draw_text(text,font,text_col,x,y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))





#game loop
while True:
    if game_paused == True:
        pass #dispaly menu
    else:

        draw_text("MENU",FONT,TEXT_COL, 135,150)


#evnt handler
    for event in pygame.event.get():

        if event.type ==pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                game_paused = True

        if event.type == pygame.QUIT:
            quit()



    pygame.display.update()


pygame.quit()