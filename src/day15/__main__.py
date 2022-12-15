import re

DIGITS = re.compile(r"-?\d+")
data = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15\nSensor at x=9, y=16: closest beacon is at x=10, y=16\nSensor at x=13, y=2: closest beacon is at x=15, y=3\nSensor at x=12, y=14: closest beacon is at x=10, y=16\nSensor at x=10, y=20: closest beacon is at x=10, y=16\nSensor at x=14, y=17: closest beacon is at x=10, y=16\nSensor at x=8, y=7: closest beacon is at x=2, y=10\nSensor at x=2, y=0: closest beacon is at x=2, y=10\nSensor at x=0, y=11: closest beacon is at x=2, y=10\nSensor at x=20, y=14: closest beacon is at x=25, y=17\nSensor at x=17, y=20: closest beacon is at x=21, y=22\nSensor at x=16, y=7: closest beacon is at x=15, y=3\nSensor at x=14, y=3: closest beacon is at x=15, y=3\nSensor at x=20, y=1: closest beacon is at x=15, y=3"
data = open("./src/day15/input.txt").read()
test_y = 2000000


sensors = [tuple(map(int, DIGITS.findall(line))) for line in data.splitlines()]
print(len(sensors))
beacons = set((x, y) for _, _, x, y in sensors)
print(len(beacons))


def cov(sx, sy, bx, by):
    d = abs(bx - sx) + abs(by - sy)
    y = test_y
    for x in range(sx - d, sx + d + 1):
        # for y in range(sy - d, sy + d + 1):
        if abs(x - sx) + abs(y - sy) <= d:
            yield x, y

coverage = set()
for sx, sy, bx, by in sensors:
    coverage.update(cov(sx, sy, bx, by))


# coverage = set(
#     (x, y)
#     for sx, sy, bx, by in sensors
#     if (d := abs(bx - sx) + abs(by - sy))
#     for x in range(sx - d, sx + d + 1)
#     for y in range(sy - d, sy + d + 1)
#     if abs(x - sx) + abs(y - sy) <= d
# )
print("a")
coverage.difference_update(beacons)
print("b")
print(sum(1 for _, y in coverage if y == test_y))


# 5144286
