import pygame
import random
from constants import *

def red_alien_appear():
    posX, posY = WIDTH, random.randint(0, HEIGHT - ALIEN_HEIGHT)
    thisAlien = pygame.Rect(posX, posY, ALIEN_WIDTH, ALIEN_HEIGHT)
    redAliens.append(thisAlien)

def red_alien_move():
    for red_alien in redAliens:
        red_alien.x -= RED_ALIEN_VEL

def draw_alien():
    for red_alien in redAliens:
        WIN.blit(RED_ALIEN, (red_alien.x, red_alien.y))