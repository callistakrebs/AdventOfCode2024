import time

DIRECTIONS = {
    '<': (0, -1),
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0)
}

def is_in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def display_grid(grid):
    for row in grid:
        print("".join(row))
    time.sleep(0.1)

def move_rock(grid, r, c, move):
    """
    Recursively move all rocks in a row/column until an empty space is found.
    Each rock in the chain will be moved one step at a time in the given direction.
    """
    # Base case: check if out of bounds or blocked by wall
    dr, dc = DIRECTIONS[move]
    nr, nc = r + dr, c + dc
    
    if not is_in_bounds(grid, nr, nc) or grid[nr][nc] == "#":
        return False  # Stop moving if out of bounds or if a wall is encountered

    # If the next cell is empty, move the current rock to the empty space
    if grid[nr][nc] == ".":
        grid[nr][nc] = "O"  # Move the rock to the empty space
        grid[r][c] = "."     # Vacate the previous position
        return True
    
    # Otherwise, there's another rock in the way, so move the next rock in the chain
    return move_rock(grid, nr, nc, move)

def main():
    with open("day15.txt") as f:
        grid_data, moves_data = f.read().split("\n\n")
        grid = [list(row) for row in grid_data.split("\n")]
        moves = list(''.join(moves_data.split()))

    nrows = len(grid)
    ncols = len(grid[0])

    # Find initial robot position
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == "@":
                curr_r, curr_c = r, c
                break

    # Process each move
    for move in moves:
        dr, dc = DIRECTIONS[move]
        nr, nc = curr_r + dr, curr_c + dc

        if is_in_bounds(grid, nr, nc) and grid[nr][nc] != "#":
            if grid[nr][nc] == ".":
                # Move robot to the empty space
                grid[nr][nc] = grid[curr_r][curr_c]
                grid[curr_r][curr_c] = "."
                curr_r, curr_c = nr, nc
            elif grid[nr][nc] == "O":
                # Move rocks first using recursion
                if move_rock(grid, nr, nc, move):
                    # Move robot only after the rocks are moved
                    grid[nr][nc] = grid[curr_r][curr_c]
                    grid[curr_r][curr_c] = "."
                    curr_r, curr_c = nr, nc

        # display_grid(grid)  # Optional: Uncomment for debugging

    # Calculate final sum
    total = 0
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == "O":
                total += 100 * r + c

    print(total)

if __name__ == "__main__":
    main()
