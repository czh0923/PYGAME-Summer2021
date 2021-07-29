from utils.settings import TOOLBAR_HEIGHT
import pygame

def draw_toolbar(WIN, COLOR, WIDTH, TOOLBAR_HEIGHT):
    pygame.draw.rect(WIN, COLOR, (0, WIDTH + 1, WIDTH, TOOLBAR_HEIGHT))

    #pygame.display.update()