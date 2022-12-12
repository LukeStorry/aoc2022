data = open("./src/day12/input.txt").read()
map = data.splitlines()
start = next((line.index("S"), y) for y, line in enumerate(map) if "S" in line)
end = next((line.index("E"), y) for y, line in enumerate(map) if "E" in line)

map = data.replace("S", "a").replace("E", "z").splitlines()


def solve(part2: bool):
    queue, visited = [(0, end)], set()
    while queue:
        distance, (x, y) = queue.pop(0)
        if (x, y) == start or (part2 and map[y][x] == "a"):
            return distance

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < len(map[0])
                and 0 <= new_y < len(map)
                and (ord(map[y][x]) - ord(map[new_y][new_x]) <= 1)
            ):
                queue.append((distance + 1, (new_x, new_y)))


print(solve(part2=False))
print(solve(part2=True))
