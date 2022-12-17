data = list(open("./src/day17/input.txt").read())
data = list(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")

rocks = [
    ["####"],
    [".#.", "###", ".#."],
    ["..#", "..#", "###"],
    ["#", "#", "#", "#"],
    ["##", "##"],
]


width = 7
heights = [0 for _ in range(width)]


def has_halted(rock_type: int, x: int, y: int) -> bool:
    if rock_type == 1 and heights[x + 2] >= y:
        return True
    return any(
        True
        for char_x, char in enumerate(rocks[rock_type][-1])
        if char == "#" and heights[x + char_x] >= y
    )


number_of_rocks = 0
blows = 0
while number_of_rocks < 5:
    x, y = 2, max(heights) + 4
    while True:
        rock_type = number_of_rocks % 5
        x += 1 if data[blows % len(data)] == ">" else -1
        print(number_of_rocks, data[blows % len(data)])
        # print(x, y)

        blows += 1

        rock_width = max(len(row) for row in rocks[rock_type])
        x = max(0, min(x, width - rock_width))

        if has_halted(rock_type, x, y):
            break

        y -= 1

        if has_halted(rock_type, x, y):
            break
    print(x, y)
    for char_y, row in enumerate(reversed(rocks[rock_type])):
        for char_x, char in enumerate(row):
            if char == "#":
                heights[x + char_x] = max(heights[x + char_x], y + char_y + 1)

    print(number_of_rocks, heights)
    print()
    number_of_rocks += 1

print(max(heights))
# 3068
