import pygame

def build_grid(grid, ROWS, COLS, COLOR):

    for i in range(ROWS):
        grid.append([])
        for j in range(COLS):
            grid[i].append(COLOR)
    
    return grid

def draw_grid(grid, WIN, ROWS, COLS, GRID_SIZE):
    for i in range(ROWS):
        for j in range(COLS):
            pygame.draw.rect(WIN, grid[i][j], (0 + j * GRID_SIZE, 0 + i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            
    #pygame.display.update()

def clear_grid(grid, ROWS, COLS, COLOR):
    grid = []

    return build_grid(grid, ROWS, COLS, COLOR)


def draw_grid_lines(WIN, ROWS, COLS, line_color, WIDTH, HEIGHT, GRID_SIZE):

    for i in range(ROWS + 1):
        pygame.draw.line(WIN, line_color, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE))
        # if i > ROWS - 5:
        #     pygame.draw.line(WIN, (255, 0, 0), (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE))
    
    for j in range(COLS + 2):
        pygame.draw.line(WIN, line_color, (j * GRID_SIZE, 0), (j * GRID_SIZE, HEIGHT))
        # if j > ROWS - 5:
        #     pygame.draw.line(WIN, (255, 0, 0), (j * GRID_SIZE, 0), (j * GRID_SIZE, HEIGHT))
        #     print(j, GRID_SIZE, j * GRID_SIZE)

    #pygame.display.update()
