from utils import *
from grid import *
from toolbar import *
from draw_color import *
import os
import json

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Program")
print(ROWS, '*', ROWS)

def save_file(grid):
    save_path = 'histories'
    file_name = str(input("Save as? "))
    file_dir = os.path.join(save_path, file_name)

    f = open(file_dir, "w")
    json.dump(grid, f)

def load_file():
    save_path = 'histories'
    file_name = str(input("File name?"))
    file_dir = os.path.join(save_path, file_name)

    f = open(file_dir, "r")
    return json.load(f)


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
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        action = handle_button(x, y, COLOR_BUTTON, WHITE, COLORS)

                        if action == 1: # clear
                            grid = clear_grid(grid, ROWS, COLS, WHITE)
                            print('Cleared!')

                        elif action == 2: # save file
                            save_file(grid)
                            print('Saved!')
                            
                        elif action == 3: # load file
                            grid = load_file()
                            print('Loaded!')

                        elif action is None: # clicked on the margin
                            pass # do nothing

                        else:
                            draw_color = action

        draw_grid(grid, WIN, ROWS, COLS, GRID_SIZE)

        if DRAW_GRID_LINES:
            draw_grid_lines(WIN, ROWS, COLS, BLACK, WIDTH, HEIGHT, GRID_SIZE)

        draw_toolbar(WIN, WHITE, WIDTH, TOOLBAR_HEIGHT)

        draw_buttons(WIN, WIDTH, HEIGHT, TOOLBAR_HEIGHT, BUTTON_SIZE, COLORS, BUTTON_NUM, TEXT_FONT, COLOR_BUTTON, BUTTON_MARGRIN)

        pygame.display.update()

if __name__ == "__main__":
    main()
