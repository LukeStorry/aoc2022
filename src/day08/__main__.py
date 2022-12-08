data = open("./src/day08/input.txt").read()
# data = "30373\n25512\n65332\n33549\n35390"

trees = [list(map(int, line)) for line in data.splitlines()]
width, height = len(trees[0]), len(trees)


def hidden(y, x):
    left = any(1 for _x in range(x) if trees[y][_x] >= trees[y][x])
    right = any(1 for _x in range(x + 1, width) if trees[y][_x] >= trees[y][x])
    up = any(1 for _y in range(y) if trees[_y][x] >= trees[y][x])
    down = any(1 for _y in range(y + 1, height) if trees[_y][x] >= trees[y][x])
    return left and right and up and down


print(sum(1 for x in range(width) for y in range(height) if not hidden(y, x)))


def scenic(y, x):
    left = next(
        (
            i + 1
            for (i, _x) in enumerate(reversed(range(x)))
            if trees[y][_x] >= trees[y][x]
        ),
        x,
    )
    right = next(
        (
            i + 1
            for (i, _x) in enumerate(range(x + 1, width))
            if trees[y][_x] >= trees[y][x]
        ),
        width - x - 1,
    )
    up = next(
        (
            i + 1
            for (i, _y) in enumerate(reversed(range(y)))
            if trees[_y][x] >= trees[y][x]
        ),
        y,
    )
    down = next(
        (
            i + 1
            for (i, _y) in enumerate(range(y + 1, height))
            if trees[_y][x] >= trees[y][x]
        ),
        height - y - 1,
    )
    return left * right * up * down


print(max(scenic(y, x) for x in range(width) for y in range(height)))
