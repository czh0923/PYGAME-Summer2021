import pygame
from constants import *

bullets = []

def one_bullet():
    posX, posY = red.x + SPACESHIP_WIDTH, red.y + SPACESHIP_HEIGHT // 2
    thisBullet = pygame.Rect(posX, posY, 10, 5)
    bullets.append(thisBullet)

def bullet_appear():
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[key_fire]:
        one_bullet()

def bullet_appear_one_at_a_time(event):
    if event.key == key_fire:
        one_bullet()
    
def bullet_move():
    for bullet in bullets:
        bullet.x += bullet_VEL

# combine bullet_appear and bullet_move
# use to create long bullets
def handle_bullets():
    bullet_appear()
    bullet_move()

def draw_bullets(WIN):
    for bullet in bullets:
        pygame.draw.rect(WIN, RED_COLOR, bullet)
