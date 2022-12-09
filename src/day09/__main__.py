from pathlib import Path

data = open("./src/day09/input.txt").read()
# data = "R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2"

moves = [
    direction
    for [direction, _, *amount] in data.splitlines()
    for _ in range(int("".join(amount)))
]

hx, hy, tx, ty = 0, 0, 0, 0
visited = set()

for move in moves:
    match move:
        case "U":
            if hy > ty:
                ty += 1
                tx = hx
            hy += 1
        case "D":
            if hy < ty:
                ty -= 1
                tx = hx
            hy -= 1
        case "R":
            if hx > tx:
                tx += 1
                ty = hy
            hx += 1
        case "L":
            if hx < tx:
                tx -= 1
                ty = hy
            hx -= 1

    visited.add((tx, ty))

print(len(visited))
