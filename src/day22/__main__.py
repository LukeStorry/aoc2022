from math import cos, pi, sin
import re

data = open("./src/day22/input.txt").read()
tiles = {x + y * 1j for y, line in enumerate(data.splitlines()) for x, c in enumerate(line) if c == "."}
rocks = {x + y * 1j for y, line in enumerate(data.splitlines()) for x, c in enumerate(line) if c == "#"}
direction, location = 0, next(l for l in tiles if l.imag == 0)
for distance, turn in re.findall(r"(\d+)([RL]?)", data.splitlines()[-1]):
    step = int(cos(direction)) + 1j * int(sin(direction))
    for _ in range(int(distance)):
        next = location + step
        if next in rocks:
            break
        if next not in tiles:
            next -= 200 * step
            while next not in tiles.union(rocks):
                next += step
        if next in rocks:
            break
        location = next
    direction += pi / 2 if turn == "R" else -pi / 2

print(int(location.imag + 1) * 1000 + int(location.real + 1) * 4 + [1, -1j, -1, 1j].index(step))
