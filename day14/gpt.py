import re

def parse_position_and_velocity(line):
    pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    return tuple(map(int, re.findall(pattern, line)[0]))

def simulate_positions(robots, time_step):
    positions = []
    for start_x, start_y, velocity_x, velocity_y in robots:
        end_x = start_x + time_step * velocity_x
        end_y = start_y + time_step * velocity_y
        positions.append((end_x, end_y))
    return positions

def bounding_box(positions):
    xs = [x for x, y in positions]
    ys = [y for x, y in positions]
    return min(xs), max(xs), min(ys), max(ys)

def draw_grid(positions):
    min_x, max_x, min_y, max_y = bounding_box(positions)
    grid_width = max_x - min_x + 1
    grid_height = max_y - min_y + 1
    grid = [["." for _ in range(grid_width)] for _ in range(grid_height)]
    for x, y in positions:
        grid[y - min_y][x - min_x] = "O"
    return "\n".join("".join(row) for row in grid)

if __name__ == "__main__":
    with open("day14.txt") as f:
        robots = [parse_position_and_velocity(line) for line in f.read().strip().split("\n")]

    min_bounding_area = float("inf")
    best_time_step = None
    best_positions = None

    for time_step in range(7500, 10404):
        positions = simulate_positions(robots, time_step)
        min_x, max_x, min_y, max_y = bounding_box(positions)
        bounding_area = (max_x - min_x + 1) * (max_y - min_y + 1)

        if bounding_area < min_bounding_area:
            min_bounding_area = bounding_area
            best_time_step = time_step
            best_positions = positions

    print(f"Alignment detected at time step {best_time_step}:")
    print(draw_grid(best_positions))
