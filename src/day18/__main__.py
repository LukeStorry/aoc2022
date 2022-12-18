import re

cubes = set(
    (int(x), int(y), int(z))
    for x, y, z in re.findall(
        r"(\d+),(\d+),(\d+)", open("./src/day18/input.txt").read()
    )
)
sides = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
surfaces = [
    c
    for x, y, z in cubes
    for c in ((x + dx, y + dy, z + dz) for dx, dy, dz in sides)
]
print(sum(1 for c in surfaces if c not in cubes))

low, high = min((min(c) for c in cubes)) - 1, max((max(c) for c in cubes)) + 1
stop, outside = False, set([(low, low, low)])
while not stop:
    stop = True
    for x, y, z in list(outside):
        for dx, dy, dz in sides:
            neighbor = (x + dx, y + dy, z + dz)
            if (
                neighbor not in cubes
                and neighbor not in outside
                and all(low <= n <= high for n in neighbor)
            ):
                outside.add(neighbor)
                stop = False

print(sum(1 for e in surfaces if e in outside))
