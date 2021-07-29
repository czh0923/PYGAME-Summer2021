import pygame
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 600, 700
TOOLBAR_HEIGHT = HEIGHT - WIDTH
FPS = 60
# PIXEL_WIDTH, PIXEL_HEIGHT = 20, 20
ROWS = COLS = 40
GRID_SIZE = WIDTH / ROWS

DRAW_GRID_LINES = True

BUTTON_SIZE = 50
BUTTON_NUM = 7
TEXT_FONT = pygame.font.SysFont("comicsans", 15)

# color setup
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [BLACK, RED, GREEN, BLUE, WHITE]