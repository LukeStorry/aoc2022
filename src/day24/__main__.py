from dataclasses import dataclass
import re

DIGITS = re.compile(r"\d+")


@dataclass
class XYZ:
    x: int
    y: int

    def one(self, s):
        d = int(DIGITS.findall(s)[0])


data = open("./src/day24/input.txt").read().splitlines()
# data = "#.######\n#>>.<^<#\n#.<..<<#\n#>v.><>#\n#<^v^^>#\n######.#".splitlines()
# data = "#.#####\n#.....#\n#>....#\n#.....#\n#...v.#\n#.....#\n#####.#".splitlines()

blizzards = [
    ((x - 1, y - 1), c) for y, line in enumerate(data) for x, c in enumerate(line) if c in "<>v^"
]
width, height = len(data[0]) - 2, len(data) - 2
blizzards_in_time: list[set[tuple[int, int]]] = []
for blizzard_cycle in range(500):
    blizzards = [
        (
            ((x - 1) % width, y)
            if c == "<"
            else ((x + 1) % width, y)
            if c == ">"
            else (x, (y + 1) % height)
            if c == "v"
            else (x, (y - 1) % height),
            c,
        )
        for (x, y), c in blizzards
    ]
    coord_set = {xy for xy, _ in blizzards}
    if coord_set in blizzards_in_time:
        print("blizzard cycle: ", blizzard_cycle)
        break
    blizzards_in_time.append(coord_set)

queue = [(wait, 0, 0) for wait in range(5)]
queue = [(2, 0, 0)]
visited = set()
while queue:
    step, x, y = queue.pop(0)
    print("step", step, x, y)

    for (_x, _y) in ((x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if (_x, _y) == (width, height):
            print("FINISHED: ", step + 1)
            exit()
        if _x < 0 or _x > width or _y < 0 or _y >= height:
            continue
        if (_x, _y) in blizzards_in_time[(step + 1) % blizzard_cycle]:
            continue
        next_step = (step + 1, _x, _y)
        if next_step in visited:
            continue
        visited.add(next_step)
        queue.append(next_step)

print()

# 189 too low??
