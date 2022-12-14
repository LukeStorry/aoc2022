import re

data = "498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9"
data = open("./src/day14/input.txt").read()

blocked = set(
    (x, y)
    for line in data.splitlines()
    if (coords := re.findall(r"(\d+),(\d+)", line))
    for (x1, y1), (x2, y2) in zip(coords, coords[1:])
    if (ys := sorted((int(y1), int(y2)))) and (xs := sorted((int(x1), int(x2))))
    for y in range(ys[0], ys[1] + 1)
    for x in range(xs[0], xs[1] + 1)
)

max_y = max(y for _, y in blocked) + 1
sands = set()
part1 = None
while True:
    x, y = (500, 0)
    while y < max_y:
        for option in ((x, y + 1), (x - 1, y + 1), (x + 1, y + 1)):
            if option not in blocked:
                x, y = option
                break
        else:
            break
    else:
        part1 = part1 or len(sands)

    sands.add((x, y))
    blocked.add((x, y))

    if y == 0:
        print(f"{part1}, {len(sands)}")
        break

    print(
        "\n".join(
            f"{_y:03} "
            + "".join(
                "o" if (_x, _y) in sands else "#" if (_x, _y) in blocked else " "
                for _x in range(330, 675)
            )
            for _y in range(0, max_y + 1)
        )
    )
