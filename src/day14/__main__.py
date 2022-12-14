import re

data = "498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9"
data = open("./src/day14/input.txt").read()

rocks = set()
for line in data.splitlines():
    coords = [tuple(map(int, match)) for match in re.findall(r"(\d+),(\d+)", line)]
    for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
        if x1 == x2:
            frm, to = sorted([y1, y2])
            new_rocks = [(x1, y) for y in range(frm, to + 1)]
        else:
            frm, to = sorted([x1, x2])
            new_rocks = [(x, y1) for x in range(frm, to + 1)]
        rocks.update(new_rocks)


max_y = max(y for _, y in rocks)
sands = set()
while True:
    x, y = (500, 0)

    while y < max_y:
        if (x, y + 1) not in rocks.union(sands):
            y += 1
        elif (x - 1, y + 1) not in rocks.union(sands):
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in rocks.union(sands):
            x, y = x + 1, y + 1
        else:
            break
    else:
        print(f"FALL! {(x, y)}")
        break
    sands.add((x, y))

print(len(sands))


if True:
    min_x, max_x, max_y = (
        min(x for x, _ in rocks.union(sands)),
        max(x for x, _ in rocks.union(sands)),
        max(y for _, y in rocks.union(sands)),
    )
    print(
        "\n".join(
            str(y)
            + "".join(
                "#" if (x, y) in rocks else "o" if (x, y) in sands else "."
                for x in range(min_x, max_x + 1)
            )
            for y in range(0, max_y + 1)
        )
    )
    print()
