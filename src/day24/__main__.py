data = open("./src/day24/input.txt").read().splitlines()
current_blizzards = [(c, x - 1, y - 1) for y, line in enumerate(data) for x, c in enumerate(line) if c in "<>v^"]
blizzards, width, height = [], len(data[0]) - 2, len(data) - 2
while (coords := {(x, y) for _, x, y in current_blizzards}) not in blizzards:
    blizzards.append(coords)
    current_blizzards = [
        (
            c,
            (x - 1) % width if c == "<" else (x + 1) % width if c == ">" else x,
            (y + 1) % height if c == "v" else (y - 1) % height if c == "^" else y,
        )
        for c, x, y in current_blizzards
    ]
end, got_out, got_back = (width, height - 1), False, False
queue, visited = [(0, 0, 0)], set()
while queue:
    step, x, y = queue.pop(0)

    if (x, y) == end and not got_out:
        got_out = True
        print("Got to end: ", step)
        queue = [(step + 1, x, y)]
    if (x, y) == (0, 0) and got_out and not got_back:
        got_back = True
        print("Back to start: ", step)
        queue = [(step + 1, x, y)]
    if (x, y) == end and got_out and got_back:
        print("Got to end again: ", step)
        break

    for (nx, ny) in ((x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if nx < 0 or nx > width or ny < 0 or ny >= height:
            continue
        if (nx, ny) in blizzards[(step) % len(blizzards) - 1]:
            continue
        next_step = (step + 1, nx, ny)
        if next_step in visited:
            continue
        visited.add(next_step)
        queue.append(next_step)
