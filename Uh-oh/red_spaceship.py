import pygame
import random
from constants import *

def draw_red_spaceship():
    WIN.blit(RED_SPACESHIP, (red.x, red.y))


def red_move():

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[key_left] and red.x - VEL > 0:
        red.x -= VEL

    if keys_pressed[key_right] and red.x + VEL + SPACESHIP_WIDTH < WIDTH:
        red.x += VEL
    
    if keys_pressed[key_up] and red.y - VEL > 0:
        red.y -= VEL
    
    if keys_pressed[key_down] and red.y + VEL + SPACESHIP_HEIGHT < HEIGHT:
        red.y += VEL




# let the plane move randomly
def red_move_random():
    direction = random.randint(1, 4)

    
    if direction == 1 and red.x - VEL > 0: # left
        red.x -= VEL

    if direction == 2 and red.x + VEL < WIDTH: # right
        red.x += VEL
    
    if direction == 3 and red.y - VEL > 0: # up
        red.y -= VEL
    
    if direction == 4 and red.y + VEL < HEIGHT: # down
        red.y += VEL
