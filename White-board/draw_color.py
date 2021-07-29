
def draw(grid, pos, GRID_SIZE, draw_color):
    x, y = pos

    row = int(y // GRID_SIZE)
    col = int(x // GRID_SIZE)

    grid[row][col] = draw_color