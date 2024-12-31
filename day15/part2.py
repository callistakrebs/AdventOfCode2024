import time
import numpy as np

DIRECTIONS = {
    '<': (0,-1),
    '^': (-1,0),
    '>': (0,1),
    'v': (1,0)
}

def is_in_bounds(grid, r,c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def display_grid(grid):
    for row in grid:
        print("".join(row))
    time.sleep(0.1)

def move_rock_h(grid, r, c, move):
    dr, dc = DIRECTIONS[move]
    nr, nc =  r + dr*2, c + dc*2
    space_start = nc if nc <= c else c
    space_end = nc if nc >= c else c

    if not is_in_bounds(grid, nr, nc):
        return False
    
    if grid[nr][nc] == "#":
        return False
    
    if grid[r][c] == "]":
        # slice left
        start_rock = c - 1
        end_rock = c + 1
    
    if grid[r][c] == "[":
        # slice right
        start_rock = c
        end_rock = c + 2
        space_start += 1
        space_end += 1

    if grid[nr][nc] == ".":
        grid[r,space_start : space_end] = grid[r, start_rock : end_rock] #grid[r, c - 1 : c +1]
        return True

    if move_rock_h(grid, nr, nc, move):
        grid[r,space_start : space_end] = grid[r, start_rock : end_rock] #grid[r, c - 1 : c +1]
        return True

def move_rock_v(grid, r, c, move):
    dr, dc = DIRECTIONS[move]
    nr, nc = r + dr, c + dc

    if not is_in_bounds(grid, nr, nc):
        return False
    
    if grid[nr][nc] == "#":
        return False
    
    if grid[r][c] == "]": # slice left
        start_rock = c - 1
        end_rock = c + 1
    
    if grid[r][c] == "[": # slice right
        start_rock = c
        end_rock = c + 2

    if (grid[nr, start_rock:end_rock] == np.array([".","."])).all():
        # import pdb; pdb.set_trace()
        grid[nr, start_rock:end_rock] = grid[r, start_rock : end_rock]
        grid[r, start_rock : end_rock] = np.array([".","."])
        return True
    
    if (grid[nr, start_rock:end_rock] == np.array([".","["])).all():
        nc = end_rock - 1
        # return move_rock_v(grid, nr, end_rock - 1, move)
    if (grid[nr, start_rock:end_rock] == np.array(["]","."])).all():
        nc = start_rock
        # return move_rock_v(grid, nr, start_rock, move)

    if move_rock_v(grid, nr, nc, move):
        grid[nr, start_rock:end_rock] = grid[r, start_rock : end_rock]
        # import pdb; pdb.set_trace()
        grid[r, start_rock : end_rock] = np.array([".","."])
        return True

def move_rock(grid, r, c, move):
    if move == "^" or move == "v":
        return move_rock_v(grid, r, c,move)
    else:
        return move_rock_h(grid,r,c,move)

if __name__ == "__main__":
    with open("day15_debug.txt") as f:
        grid, moves = tuple(f.read().split("\n\n"))

        d_grid = []
        for row in grid.split("\n"):
            d_row = []
            for i in range (len(row)):
                if row[i] == "#" or row[i] == ".":
                    d_row = d_row + [row[i]] * 2
                if row[i] == "O":
                    d_row = d_row + ["[","]"]
                if row[i] == "@":
                    d_row = d_row + ["@","."]
            d_grid.append(d_row)
        
        d_grid = np.array(d_grid)
        moves = list(''.join(moves.split()))

    nrows = len(d_grid)
    ncols = len(d_grid[0])

    for r in range(nrows):
        for c in range (ncols):
            if d_grid[r][c] == "@":
                curr_r, curr_c = r,c

    for move in moves:
        dr, dc = DIRECTIONS[move]
        nr, nc = curr_r + dr, curr_c + dc
        if is_in_bounds(d_grid, nr, nc):
            if d_grid[nr][nc] == "#":
                continue # can't move here

            if d_grid[nr][nc] == ".":
                d_grid[nr][nc] = d_grid[curr_r][curr_c]
                d_grid[curr_r][curr_c] = "."
                curr_r, curr_c = nr, nc
            
            if d_grid[nr][nc] == "[" or d_grid[nr][nc] == "]":
                if d_grid[nr][nc] == "[":
                    v_replace = np.array(["@", "."])
                    start = nc
                    end = nc+2
                else:
                    v_replace = np.array([".", "@"])
                    start = nc -1
                    end = nc +1
                    
                if (move_rock(d_grid, nr, nc, move)):
                    # move robot only if the rock moved
                    if move == "<" or move == ">":
                        # import pdb; pdb.set_trace()
                        d_grid[nr][nc] = d_grid[curr_r][curr_c]
                        d_grid[curr_r][curr_c] = "."
                        curr_r, curr_c = nr, nc
                    else:
                        d_grid[nr,start: end] = v_replace
                        d_grid[curr_r][curr_c] = "."
                        curr_r, curr_c = nr, nc
        display_grid(d_grid) 

    sum = 0
    for row in range (nrows):
        for col in range (ncols):
            if grid[row][col] == "O":
                sum += 100*row + col

    print(sum)