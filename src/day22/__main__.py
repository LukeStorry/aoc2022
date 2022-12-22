import re

data = open("./src/day22/input.txt").read()
tiles = {x + y * 1j for y, line in enumerate(data.splitlines(), 1) for x, c in enumerate(line, 1) if c == "."}
rocks = {x + y * 1j for y, line in enumerate(data.splitlines(), 1) for x, c in enumerate(line, 1) if c == "#"}
moves = re.findall(r"(\d+)([RL]?)", data.splitlines()[-1])


def cube_wrapping(location, step):
    x, y = (location).real, (location).imag
    match step:
        case 1:
            if 1 <= y <= 50:
                return 100 + 151j - 1j * y, -1
            if 51 <= y <= 100:
                return y + 50 + 50j, -1j
            if 101 <= y <= 150:
                return 150 + 151j - y * 1j, -1
            if 151 <= y <= 200:
                return y - 100 + 150j, -1j
        case -1:
            if 1 <= y <= 50:
                return 151j - y * 1j + 1, 1
            if 51 <= y <= 100:
                return 101j + y - 50, 1j
            if 101 <= y <= 150:
                return 151j - y * 1j + 51, 1
            if 151 <= y <= 200:
                return 1j + y - 100, 1j
        case -1j:
            if 1 <= x <= 50:
                return 50j + x * 1j + 51, 1
            if 51 <= x <= 100:
                return x * 1j + 100j + y, 1
            if 101 <= x <= 150:
                return 200j + x - 100, -1j
        case 1j:
            if 1 <= x <= 50:
                return 1j + x + 100, 1j
            if 51 <= x <= 100:
                return x * 1j + 100j + 50, -1
            if 101 <= x <= 150:
                return x * 1j - 50j + 100, -1


def solve(part1):
    step, location = 1, next(l for l in tiles if l.imag == 1)
    for distance, turn in moves:
        for _ in range(int(distance)):
            next_location = location + step
            if next_location in rocks:
                break
            if next_location not in tiles:
                if part1:
                    next_location -= 200 * step
                    while next_location not in tiles:
                        next_location += step
                    if next_location - step in rocks:
                        break
                else:
                    next_location, next_step = cube_wrapping(next_location - step, step)
                    if next_location not in rocks:
                        step = next_step
                    else:
                        break

            location = next_location

        step *= 1j if turn == "R" else -1j if turn == "L" else 1
    return int(location.imag) * 1000 + int(location.real) * 4 + [1, 1j, -1, -1j].index(step)


print(solve(part1=True))
print(solve(part1=False))
