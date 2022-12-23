from collections import defaultdict

data = open("./src/day23/input.txt").read()
elves = {(x, y) for y, line in enumerate(reversed(data.splitlines())) for x, c in enumerate(line) if c == "#"}

for i in range(10000):
    choices = defaultdict(list)
    next_elves = set()
    for x, y in elves:
        directions = [
            ((x, y + 1), ((x - 1, y + 1), (x, y + 1), (x + 1, y + 1))),  # North
            ((x, y - 1), ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1))),  # South
            ((x - 1, y), ((x - 1, y - 1), (x - 1, y), (x - 1, y + 1))),  # West
            ((x + 1, y), ((x + 1, y - 1), (x + 1, y), (x + 1, y + 1))),  # East
        ]
        if not any(check in elves for _, checks in directions for check in checks):
            next_elves.add((x, y))
            continue
        for result, checks in directions[i % 4 :] + directions[: i % 4]:
            if not any(e in elves for e in checks):
                choices[result].append((x, y))
                break
        else:
            next_elves.add((x, y))

    if not choices:
        break

    for choice, elves_with_choice in choices.items():
        if len(elves_with_choice) == 1:
            next_elves.add(choice)
        else:
            next_elves.update(elves_with_choice)

    elves = next_elves

    if i == 9:
        print(
            "Part 1: ",
            sum(
                1
                for x in range(min(x for x, _ in elves), max(x for x, _ in elves) + 1)
                for y in range(min(y for _, y in elves), max(y for _, y in elves) + 1)
                if not any((x, y) == e for e in elves)
            ),
        )

print("Part 2: ", i + 1)
