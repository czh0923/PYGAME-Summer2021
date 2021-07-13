import pygame
import os

''' Game setup '''
key_up = pygame.K_w
key_down = pygame.K_s
key_left = pygame.K_a
key_right = pygame.K_d

key_fire = pygame.K_j


''' Window setup'''
WIDTH, HEIGHT = 900, 500
FPS = 60 # Frames per second
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane War!")


''' background setup'''
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


''' red_spaceship setup '''
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VEL = 5 # spaceship velocity
red = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

# spaceship image setup
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 270)


''' bullet setup '''
RED_COLOR = (255, 0, 0)
bullet_VEL = 7

