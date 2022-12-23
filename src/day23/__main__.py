from dataclasses import dataclass


@dataclass(slots=True)
class Elf:
    location: complex
    chosen_move: complex | None = None

    def choose(self, other_locations: list[complex], offset: int):
        self.chosen_move = None
        surrounding = [self.location + d for d in ((-1 + 1j), 1, 1j, (1 + 1j), (-1 - 1j), (-0 - 1j), (1 - 1j), -1)]
        if not (nearby := [l for l in other_locations if l in surrounding]):
            return
        for direction in ("N", "S", "W", "E")[offset:] + ("N", "S", "W", "E")[:offset]:
            match direction:
                case "N":
                    if not any(self.location + d in nearby for d in (1j - 1, 1j, 1j + 1)):
                        self.chosen_move = self.location + 1j
                        return
                case "S":
                    if not any(self.location + d in nearby for d in (-1j - 1, -1j, -1j + 1)):
                        self.chosen_move = self.location + -1j
                        return
                case "W":
                    if not any(self.location + d in nearby for d in (-1 - 1j, -1, -1 + 1j)):
                        self.chosen_move = self.location + -1
                        return
                case "E":
                    if not any(self.location + d in nearby for d in (1 - 1j, 1, 1 + 1j)):
                        self.chosen_move = self.location + 1
                        return

    def move(self, others: list["Elf"]):
        assert self.chosen_move is not None
        if self.chosen_move in (e.chosen_move for e in others if e != self):
            return
        self.location = self.chosen_move


data = open("./src/day23/input.txt").read()
elves = [Elf(complex(x, y)) for y, line in enumerate(reversed(data.splitlines())) for x, c in enumerate(line) if c == "#"]


for i in range(10000):
    print(i)
    locations = [e.location for e in elves]
    for elf in elves:
        elf.choose(locations, i % 4)

    elves_with_choices = [e for e in elves if e.chosen_move is not None]
    if not elves_with_choices:
        break
    for elf in elves_with_choices:
        elf.move(elves_with_choices)

    if i == 9:
        print(
            "Part 1: ",
            sum(
                1
                for x in range(int(min(e.location.real for e in elves)), int(max(e.location.real for e in elves)) + 1)
                for y in range(int(min(e.location.imag for e in elves)), int(max(e.location.imag for e in elves)) + 1)
                if not any(complex(x, y) == e.location for e in elves)
            ),
        )

print("Part 2: ", i + 1)
