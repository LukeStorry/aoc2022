data = list(open("./src/day17/input.txt").read())
# data = list(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")

rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]

width, number_of_rocks, blows = 7, 0, 0
heights, taken_places = [0] * 7, set((x, 0) for x in range(width))

blocked = lambda rock_type, x, y: any(
    x < 0 or x + dx >= width or (x + dx, y + dy) in taken_places
    for dx, dy in rocks[rock_type]
)

while number_of_rocks < 2022:
    x, y = 2, max(heights) + 4
    while True:
        rock_type = number_of_rocks % 5
        if data[blows] == "<" and not blocked(rock_type, x - 1, y):
            x -= 1
        if data[blows] == ">" and not blocked(rock_type, x + 1, y):
            x += 1
        blows = (blows + 1) % len(data)
        if blocked(rock_type, x, y - 1):
            break
        y -= 1

    for dx, dy in rocks[rock_type]:
        heights[x + dx] = max(heights[x + dx], y + dy)
        taken_places.add((x + dx, y + dy))

    number_of_rocks += 1

print(max(heights))
# 3068
