import re

data = "498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9"
# data = open("./src/day14/input.txt").read()

rocks = set()
for line in data.splitlines():
    coords = [tuple(map(int, match)) for match in re.findall(r"(\d+),(\d+)", line)]
    for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
        if x1 == x2:
            frm, to = sorted((y1, y2))
            rocks.update((x1, y) for y in range(frm, to + 1))
        else:
            frm, to = sorted((x1, x2))
            rocks.update((x, y1) for x in range(frm, to + 1))

max_y = max(y for _, y in rocks) + 1
sands = set()
part1 = None
while True:
    x, y = (500, 0)
    blocked = rocks.union(sands)
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

    if y == 0:
        print(f"{part1}, {len(sands)}")
        break

    # / DISPLAY
    # min_x, max_x = (
    #     min(_x for _x, _ in blocked),
    #     max(_x for _x, _ in blocked),
    # )
    # print("\n" * 100)
    # print(
    #     "\n".join(
    #         str(_y)
    #         + "".join(
    #             "#" if (_x, _y) in rocks else "o" if (_x, _y) in sands else "."
    #             for _x in range(min_x, max_x + 1)
    #         )
    #         for _y in range(0, max_y + 1)
    #     )
    # )
    # print()
    # sleep(0.1)
