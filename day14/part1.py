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
    
    grid = [[0 for i in range(101)] for i in range(103)] # 11 by 7 for debug

    for startx,starty, vx, vy in pos_and_vel:
        endx = (startx + 100*vx)%101
        endy = (starty + 100*vy)%103
        grid[endy][endx] += 1
    
    midv = len(grid) // 2
    midh = len(grid[0]) // 2

    q1 = sum(sum(row[0:midh]) for row in grid[0:midv])
    q2 = sum(sum(row[midh+1:]) for row in grid[0:midv])
    q3 = sum(sum(row[0:midh]) for row in grid[midv+1:])
    q4 = sum(sum(row[midh+1:]) for row in grid[midv+1:])

    print(q1*q2*q3*q4)

    