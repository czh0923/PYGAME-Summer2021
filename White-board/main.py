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
    draw_color = BLACK
    grid = []
    clock = pygame.time.Clock()
    build_grid(grid, ROWS, COLS, WHITE)
    COLOR_BUTTON = {}

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                x, y = pos

                try:
                    draw(grid, x, y, GRID_SIZE, draw_color)
                except IndexError:
                    action = handle_button(x, y, COLOR_BUTTON, WHITE, COLORS)
                    if action == 1: # clear
                        print('Cleared')
                        grid = clear_grid(grid, ROWS, COLS, WHITE)
                    elif action == 2:
                        pass # save
                    else:
                        draw_color = action

        draw_grid(grid, WIN, ROWS, COLS, GRID_SIZE)

        if DRAW_GRID_LINES:
            draw_grid_lines(WIN, ROWS, COLS, BLACK, WIDTH, HEIGHT, GRID_SIZE)

        draw_toolbar(WIN, WHITE, WIDTH, TOOLBAR_HEIGHT)

        draw_buttons(WIN, WIDTH, HEIGHT, TOOLBAR_HEIGHT, BUTTON_SIZE, COLORS, BUTTON_NUM, TEXT_FONT, COLOR_BUTTON)

        pygame.display.update()

if __name__ == "__main__":
    main()
