import pygame
from constants import *

bullets = []

def one_bullet():
    posX, posY = red.x + SPACESHIP_WIDTH, red.y + SPACESHIP_HEIGHT // 2
    thisBullet = pygame.Rect(posX, posY, 10, 5)
    bullets.append(thisBullet)

# def bullet_appear():
#     keys_pressed = pygame.key.get_pressed()

#     if keys_pressed[key_fire]:
#         one_bullet()

# def bullet_appear_one_at_a_time(event):
#     if event.key == key_fire:
#         one_bullet()
    
def bullet_move():
    remove_bullet_lst = []
    for bullet in bullets:
        bullet.x += bullet_VEL
        handle_bullet(bullet, remove_bullet_lst)
    for remove_bullet in remove_bullet_lst:
        bullets.remove(remove_bullet)

# combine bullet_appear and bullet_move
# use to create long bullets
# def handle_bullets():
#     bullet_appear()
#     bullet_move()

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(WIN, RED_COLOR, bullet)

def handle_bullet(one_bullet, remove_bullet_lst):
    remove_alien_lst = []
    for red_aline in redAliens:
        if one_bullet.colliderect(red_aline):
            pygame.event.post(pygame.event.Event(RED_ALIEN_DIED))
            print(1)
            remove_bullet_lst.append(one_bullet)
            remove_alien_lst.append(red_aline)
    for remove_alien in remove_alien_lst:
        redAliens.remove(remove_alien)
