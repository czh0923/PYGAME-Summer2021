import pygame
import os
pygame.mixer.init()
pygame.font.init()

''' Game setup '''
key_up = pygame.K_w
key_down = pygame.K_s
key_left = pygame.K_a
key_right = pygame.K_d

key_fire = pygame.K_j

''' COLOR '''
WHITE = (255, 255, 255)
RED_COLOR = (255, 0, 0)

''' EVENTS'''
RED_ALIEN_DIED = pygame.USEREVENT + 1

''' SOUND '''
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
ALIEN_DIE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'uh_oh.mp3'))

''' Window setup'''
WIDTH, HEIGHT = 900, 500
FPS = 60 # Frames per second
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uh-oh!")

SCORE_FONT = pygame.font.SysFont('comicsans', 40)

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
bullet_VEL = 7


''' Aliens setup '''
ALIEN_WIDTH, ALIEN_HEIGHT = 40, 64

# red alien
redAliens = []
RED_ALIEN_VEL = 1
red_alien_refresh = 150 # refresh time
RED_ALIEN_SCORE = 10

RED_ALIEN_IMAGE= pygame.image.load(os.path.join('Assets', 'redalien.png'))
RED_ALIEN = pygame.transform.scale(RED_ALIEN_IMAGE, (ALIEN_WIDTH, ALIEN_HEIGHT))

