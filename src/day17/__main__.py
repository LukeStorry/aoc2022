data = list(open("./src/day17/input.txt").read())
rock_shapes = [[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (0, 1), (1, 0), (1, 1)]]
width, rocks, blows, cycles, extra_height = 7, 0, 0, {}, 0
heights, taken_places = [0] * width, set((x, 0) for x in range(width))
blocked = lambda rock_type, x, y: any(x < 0 or x + dx >= width or (x + dx, y + dy) in taken_places for dx, dy in rock_shapes[rock_type])
part1, part2 = 2022, 1000000000000

while rocks < part2:
    x, y = 2, max(heights) + 4
    while True:
        rock_type = rocks % 5
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

    rocks += 1
    if rocks in (part1, part2):
        print(max(heights) + extra_height)

    cycle = (rock_type, blows, tuple(max(heights) - h for h in heights))
    if rocks > part1 and cycle in cycles:
        cycle_rocks, cycle_height = cycles[cycle]
        repeats = ((part2 - cycle_rocks) // (rocks - cycle_rocks)) - 1
        extra_height += repeats * (max(heights) - cycle_height)
        rocks += repeats * (rocks - cycle_rocks)
    cycles[cycle] = (rocks, max(heights))
