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

def yellow_alien_appear():
    #posX, posY = WIDTH, random.randint(0, HEIGHT - ALIEN_HEIGHT)
    posX, posY = random.randint(0, WIDTH - ALIEN_WIDTH), HEIGHT
    thisAlien = pygame.Rect(posX, posY, ALIEN_WIDTH, ALIEN_HEIGHT)
    yellowAliens.append(thisAlien)

def yellow_alien_move():
    for yellow_alien in yellowAliens:
        yellow_alien.x += YELLOW_ALIEN_VEL_X
        yellow_alien.y -= YELLOW_ALIEN_VEL_Y

def draw_alien():
    for red_alien in redAliens:
        WIN.blit(RED_ALIEN, (red_alien.x, red_alien.y))
    for yellow_alien in yellowAliens:
        WIN.blit(YELLOW_ALIEN, (yellow_alien.x, yellow_alien.y))

def handle_alien_spaceship():
    for red_aline in redAliens:
        if red.colliderect(red_aline):
            pygame.event.post(pygame.event.Event(SPACESHIP_DAMAGE))
    
    for yellow_aline in yellowAliens:
        if red.colliderect(yellow_aline):
            pygame.event.post(pygame.event.Event(SPACESHIP_DAMAGE))
           