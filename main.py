import pygame
import pygame_menu
import random
import PyQt5
import menu
import os
from sys import exit


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

'''''
def draw():
    WIN.blit(menu,100,300)
'''

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome', 400, 300,theme=pygame_menu.themes.THEME_BLUE)
menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()



    pygame.display.update()
