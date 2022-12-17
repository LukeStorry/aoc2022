data = list(open("./src/day17/input.txt").read())
rock_shapes: list[list[complex]] = [[0, 1, 2, 3], [1j, 1, 1 + 1j, 1 + 2j, 2 + 1j], [0, 1, 2, 2 + 1j, 2 + 2j], [0, 1j, 2j, 3j], [0, 1j, 1, 1 + 1j]]
width, rocks, blows, extra_height, cycles = 7, 0, 0, 0, {}
heights, taken_places = [0] * width, set(x + 0j for x in range(width))
blocked = lambda rock_type, loc: any(
    (loc + block).real < 0 or (loc + block).real >= width or loc + block in taken_places
    for block in rock_shapes[rock_type]
)
part1, part2 = 2022, 1000000000000
while rocks < part2:
    location = complex(2, max(heights) + 4)
    while True:
        rock_type = rocks % 5
        if data[blows] == "<" and not blocked(rock_type, location - 1):
            location -= 1
        if data[blows] == ">" and not blocked(rock_type, location + 1):
            location += 1
        blows = (blows + 1) % len(data)
        if blocked(rock_type, location - 1j):
            break
        location -= 1j

    for block in rock_shapes[rock_type]:
        new = location + block
        heights[int(new.real)] = max(heights[int(new.real)], int(new.imag))
        taken_places.add(new)

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
