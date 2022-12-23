from collections import defaultdict

data = "....#..\n..###.#\n#...#.#\n.#...##\n#.###..\n##.#.##\n.#..#.."
data = open("./src/day23/input.txt").read()
elves = {complex(x, y) for y, line in enumerate(reversed(data.splitlines())) for x, c in enumerate(line) if c == "#"}


for i in range(10000):
    choices: dict[complex, list[complex]] = defaultdict(list)
    next_elves: set[complex] = set()
    for elf in elves:
        directions = [
            ((elf + 1j - 1, elf + 1j, elf + 1j + 1), elf + 1j),
            ((elf - 1j - 1, elf - 1j, elf - 1j + 1), elf + -1j),
            ((elf - 1 - 1j, elf - 1, elf - 1 + 1j), elf + -1),
            ((elf + 1 - 1j, elf + 1, elf + 1 + 1j), elf + 1),
        ]
        if not any(c in elves for check, _ in directions for c in check):
            next_elves.add(elf)
            continue
        for check, result in directions[i % 4 :] + directions[: i % 4]:
            if not any(e in elves for e in check):
                choices[result].append(elf)
                break
        else:
            next_elves.add(elf)

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
                for x in range(int(min(e.real for e in elves)), int(max(e.real for e in elves)) + 1)
                for y in range(int(min(e.imag for e in elves)), int(max(e.imag for e in elves)) + 1)
                if not any(complex(x, y) == e for e in elves)
            ),
        )

print("Part 2: ", i + 1)
