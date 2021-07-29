
def draw(grid, x, y, GRID_SIZE, draw_color):

    row = int(y // GRID_SIZE)
    col = int(x // GRID_SIZE)

    grid[row][col] = draw_color