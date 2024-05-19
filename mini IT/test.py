import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 8
TILE_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Match-3 Puzzle Game")

# Function to initialize the grid with random puzzle pieces
def initialize_grid():
    grid = [[random.choice([RED, GREEN, BLUE]) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    return grid

# Function to draw the grid
def draw_grid(grid):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pygame.draw.rect(screen, grid[y][x], (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Function to swap two puzzle pieces
def swap(grid, row1, col1, row2, col2):
    grid[row1][col1], grid[row2][col2] = grid[row2][col2], grid[row1][col1]

# Function to check for matches
def check_matches(grid):
    matches = []
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = grid[y][x]
            if color != BLACK:  # If not already marked for removal
                # Check horizontal matches
                if x < GRID_SIZE - 2 and grid[y][x+1] == color and grid[y][x+2] == color:
                    matches.extend([(y, x), (y, x+1), (y, x+2)])
                # Check vertical matches
                if y < GRID_SIZE - 2 and grid[y+1][x] == color and grid[y+2][x] == color:
                    matches.extend([(y, x), (y+1, x), (y+2, x)])
    return list(set(matches))  # Remove duplicates

# Function to remove matched pieces from the grid
def remove_matches(grid, matches):
    for y, x in matches:
        grid[y][x] = BLACK

# Function to drop pieces down and fill empty spaces
def drop_pieces(grid):
    for x in range(GRID_SIZE):
        column = [grid[y][x] for y in range(GRID_SIZE)]
        column = [color for color in column if color != BLACK]  # Remove empty spaces
        column = [BLACK] * (GRID_SIZE - len(column)) + column  # Fill empty spaces at the top
        for y in range(GRID_SIZE):
            grid[y][x] = column[y]

# Main game loop
def main():
    grid = initialize_grid()
    selected = None
    running = True

    while running:
        screen.fill(WHITE)
        draw_grid(grid)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // TILE_SIZE, x // TILE_SIZE

                if selected is None:
                    selected = (row, col)
                else:
                    if (abs(row - selected[0]) == 1 and col == selected[1]) or \
                       (abs(col - selected[1]) == 1 and row == selected[0]):
                        swap(grid, selected[0], selected[1], row, col)
                        matches = check_matches(grid)
                        if matches:
                            remove_matches(grid, matches)
                            drop_pieces(grid)
                            matches = check_matches(grid)
                            while matches:
                                remove_matches(grid, matches)
                                drop_pieces(grid)
                                matches = check_matches(grid)
                        selected = None
                    else:
                        selected = (row, col)

    pygame.quit()

if __name__ == "__main__":
    main()
