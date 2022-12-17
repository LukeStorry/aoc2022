data = list(open("./src/day17/input.txt").read())
data = list(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")

rock_shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]

width, n_rocks, blows = 7, 0, 0
heights, taken_places = [0] * 7, set((x, 0) for x in range(width))
cycles, extra_height = {}, 0
blocked = lambda rock_type, x, y: any(
    x < 0 or x + dx >= width or (x + dx, y + dy) in taken_places
    for dx, dy in rock_shapes[rock_type]
)

part1_rocks, part2_rocks = 2022, 1000000000000
while n_rocks < part2_rocks:
    x, y = 2, max(heights) + 4
    while True:
        rock_type = n_rocks % 5
        if data[blows] == "<" and not blocked(rock_type, x - 1, y):
            x -= 1
        if data[blows] == ">" and not blocked(rock_type, x + 1, y):
            x += 1
        blows = (blows + 1) % len(data)
        if blocked(rock_type, x, y - 1):
            break
        y -= 1

    for dx, dy in rock_shapes[rock_type]:
        heights[x + dx] = max(heights[x + dx], y + dy)
        taken_places.add((x + dx, y + dy))

    n_rocks += 1
    if n_rocks == 2022:
        print(max(heights))

    normalised_heights = tuple(h - min(heights) for h in heights)

    cycle = (rock_type, blows, normalised_heights)
    if n_rocks > part1_rocks and cycle in cycles:
        cycle_rocks, cycle_height = cycles[cycle]
        repeats = ((part2_rocks - cycle_rocks) // (n_rocks - cycle_rocks)) - 1
        extra_height += repeats * (max(heights) - cycle_height)
        n_rocks += repeats * (n_rocks - cycle_rocks)

    cycles[cycle] = (n_rocks, max(heights))


print(max(heights) + extra_height)
