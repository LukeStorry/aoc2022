from dataclasses import dataclass


@dataclass
class Knot:
    x: int
    y: int
    visited: set[tuple[int, int]]
    follower: "Knot" = None

    def move(self, direction: str):
        self.y += {"U": 1, "D": -1}.get(direction, 0)
        self.x += {"R": 1, "L": -1}.get(direction, 0)
        self.visited.add((self.x, self.y))
        self.follower.follow(self.x, self.y)

    def follow(self, x: int, y: int):
        dx, dy = x - self.x, y - self.y

        if abs(dx) > 1:
            self.x += 1 if dx > 0 else -1
        if abs(dy) > 1:
            self.y += 1 if dy > 0 else -1

        # has dx but dy bigger
        if abs(dx) >= 1 and abs(dy) > abs(dx):
            self.x = x
        # has dy but dx bigger
        elif abs(dy) >= 1 and abs(dy) < abs(dx):
            self.y = y

        self.visited.add((self.x, self.y))

        if self.follower is not None:
            self.follower.follow(self.x, self.y)


knots = [Knot(0, 0, set([(0, 0)])) for _ in range(10)]
for knot, follower in zip(knots, knots[1:]):
    knot.follower = follower

data = open("./src/day09/input.txt").read()
repeated_moves = (m[0] for m in data.splitlines() for _ in range(int(m[1:])))
for move in repeated_moves:
    knots[0].move(move)

print(len(knots[1].visited))
print(len(knots[9].visited))
