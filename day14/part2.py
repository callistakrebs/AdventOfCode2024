import re


def getPositionAndVelocity(line):
    pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    return tuple(map(int,re.findall(pattern, line)[0]))

if __name__ == "__main__":
    with open("day14.txt") as f:
        robots = f.read().split("\n")
    
    pos_and_vel = []
    for robot in robots:
        pos_and_vel.append(getPositionAndVelocity(robot))

    states = set()
    with open("output.txt", "w") as f:
        for i in range(7500,10404):
            grid = [["." for i in range(101)] for i in range(103)] # 11 by 7 for debug
            for startx,starty, vx, vy in pos_and_vel:
                endx = (startx + i*vx)%101
                endy = (starty + i*vy)%103
                grid[endy][endx] = "O"
            
            # grid_tuple = tuple(tuple(row) for row in grid)
            # if grid_tuple in states:
            #     print(i)
            #     break
            # states.add(grid_tuple)

            print(i, file=f)
            for row in grid:
                print(''.join(row), file=f)