from itertools import product
import re

cubes = set(
    (int(x), int(y), int(z))
    for x, y, z in re.findall(
        r"(\d+),(\d+),(\d+)", open("./src/day18/input.txt").read()
    )
)
sides = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
surfaces = [
    (x + dx, y + dy, z + dz)
    for (x, y, z), (dx, dy, dz) in product(cubes, sides)
]
print(sum(1 for c in surfaces if c not in cubes))

low, high = min((min(c) for c in cubes)) - 1, max((max(c) for c in cubes)) + 1
outside = set([(low, low, low)])
while True:
    if next := set(
        neighbor
        for (x, y, z), (dx, dy, dz) in product(outside, sides)
        if (
            (neighbor := (x + dx, y + dy, z + dz))
            and neighbor not in cubes
            and neighbor not in outside
            and all(low <= n <= high for n in neighbor)
        )
    ):
        outside.update(next)
    else:
        break
print(sum(1 for e in surfaces if e in outside))
