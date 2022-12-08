from math import prod

data = open("./src/day08/input.txt").read()

trees = [list(map(int, line)) for line in data.splitlines()]
width, height = len(trees[0]), len(trees)


def slices(y, x):
    return (
        [trees[y][_x] for _x in reversed(range(x))],
        [trees[y][_x] for _x in range(x + 1, width)],
        [trees[_y][x] for _y in reversed(range(y))],
        [trees[_y][x] for _y in range(y + 1, height)],
    )


def visible(x, y):
    return any(
        not any(tree >= trees[y][x] for tree in direction) for direction in slices(y, x)
    )


print(sum(1 for x in range(width) for y in range(height) if visible(x, y)))


def scenic_score(y, x):
    return prod(
        next(
            (i + 1 for (i, tree) in enumerate(direction) if tree >= trees[y][x]),
            len(direction),
        )
        for direction in slices(y, x)
    )


print(max(scenic_score(y, x) for x in range(width) for y in range(height)))
