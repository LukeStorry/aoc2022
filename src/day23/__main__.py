from dataclasses import dataclass


@dataclass
class Elf:
    location: complex
    chosen_move: complex | None = None

    def try_north(self, other_locations: list[complex]):
        if not any(self.location + d in other_locations for d in (1j, 1j + 1, 1j - 1)):
            self.chosen_move = self.location + 1j
            return True
        return False

    def try_south(self, other_locations: list[complex]):
        if not any(self.location + d in other_locations for d in (-1j, -1j + 1, -1j - 1)):
            self.chosen_move = self.location + -1j
            return True
        return False

    def try_west(self, other_locations: list[complex]):
        if not any(self.location + d in other_locations for d in (-1, -1j - 1, 1j - 1)):
            self.chosen_move = self.location + -1
            return True
        return False

    def try_east(self, other_locations: list[complex]):
        if not any(self.location + d in other_locations for d in (1, -1j + 1, 1j + 1)):
            self.chosen_move = self.location + 1
            return True
        return False

    def choose(self, other_locations: list[complex], offset: int):
        self.chosen_move = None
        surroundings = (
            1j,
            (1 + 1j),
            (-1 + 1j),
            1,
            (1 - 1j),
            (1 + 1j),
            (-0 - 1j),
            (1 - 1j),
            (-1 - 1j),
            -1,
            (-1 - 1j),
            (-1 + 1j),
        )

        if not any(self.location + d in other_locations for d in surroundings):
            return
        choices = (self.try_north, self.try_south, self.try_west, self.try_east)
        for c in choices[offset % 4 :] + choices[: offset % 4]:
            if c(other_locations):
                return

    def move(self, others: list["Elf"]):
        if self.chosen_move is None or self.chosen_move in (e.chosen_move for e in others if e != self):
            return
        self.location = self.chosen_move


data = open("./src/day23/input.txt").read()
# data = "....#..\n..###.#\n#...#.#\n.#...##\n#.###..\n##.#.##\n.#..#.."
elves = [
    Elf(complex(x, y)) for y, line in enumerate(reversed(data.splitlines())) for x, c in enumerate(line) if c == "#"
]

for i in range(1000):
    print(i)
    locations = [e.location for e in elves]
    for elf in elves:
        elf.choose(locations, i)

    elves_with_choices = [e for e in elves if e.chosen_move is not None]
    if not elves_with_choices:
        break
    for elf in elves_with_choices:
        elf.move(elves)

    if i == 9:
        print(
            sum(
                1
                for x in range(int(min(e.location.real for e in elves)), int(max(e.location.real for e in elves)) + 1)
                for y in range(int(min(e.location.imag for e in elves)), int(max(e.location.imag for e in elves)) + 1)
                if not any(complex(x, y) == e.location for e in elves)
            )
        )

print(i + 1)
