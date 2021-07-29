from utils import *
from grid import *
from toolbar import *
from draw_color import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Program")
print(ROWS, '*', ROWS)

def main():
    run = True
    WIN.fill(WHITE)
    draw_color = BLUE
    grid = []
    clock = pygame.time.Clock()
    build_grid(grid, ROWS, COLS, WHITE)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                draw(grid, pos, GRID_SIZE, draw_color)

        draw_grid(grid, WIN, ROWS, COLS, GRID_SIZE)

        if DRAW_GRID_LINES:
            draw_grid_lines(WIN, ROWS, COLS, BLACK, WIDTH, HEIGHT, GRID_SIZE)

        draw_toolbar(WIN, WHITE, WIDTH, TOOLBAR_HEIGHT)

        pygame.display.update()

if __name__ == "__main__":
    main()
