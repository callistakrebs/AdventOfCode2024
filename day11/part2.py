from functools import cache
from collections import defaultdict

@cache
def blink(stone, blinks_remaining = 75):
    nstones = 1
    if blinks_remaining <= 0:
        return nstones

    if stone == '0':
        return blink('1', blinks_remaining-1)

    elif len(stone) % 2 != 0:
        return blink(str(int(stone) * 2024), blinks_remaining-1)

    else:
        return blink(str(int(stone[len(stone) // 2:])), blinks_remaining-1) + blink(stone[0:len(stone)// 2], blinks_remaining-1)


if __name__ == "__main__":
    with open("day11.txt") as f:
        stones = f.read().split()
    
    counts = defaultdict(int)
    for stone in stones:
        counts[stone] += blink(stone)

    print(f"Total stones after 75 blinks: {sum(counts.values())}")