import re

DIGITS = re.compile(r"-?\d+")
data = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15\nSensor at x=9, y=16: closest beacon is at x=10, y=16\nSensor at x=13, y=2: closest beacon is at x=15, y=3\nSensor at x=12, y=14: closest beacon is at x=10, y=16\nSensor at x=10, y=20: closest beacon is at x=10, y=16\nSensor at x=14, y=17: closest beacon is at x=10, y=16\nSensor at x=8, y=7: closest beacon is at x=2, y=10\nSensor at x=2, y=0: closest beacon is at x=2, y=10\nSensor at x=0, y=11: closest beacon is at x=2, y=10\nSensor at x=20, y=14: closest beacon is at x=25, y=17\nSensor at x=17, y=20: closest beacon is at x=21, y=22\nSensor at x=16, y=7: closest beacon is at x=15, y=3\nSensor at x=14, y=3: closest beacon is at x=15, y=3\nSensor at x=20, y=1: closest beacon is at x=15, y=3"
data = open("./src/day15/input.txt").read()


sensors = [tuple(map(int, DIGITS.findall(line))) for line in data.splitlines()]
print(len(sensors))
beacons = set((x, y) for _, _, x, y in sensors)
print(len(beacons))

test_y = 2000000


# coverage = set()
# for sx, sy, bx, by in sensors:
#     coverage.update(cov(sx, sy, bx, by))
# coverage.difference_update(beacons)
# print(sum(1 for _, y in coverage if y == test_y))
# # 5144286


max_coord = 20
max_coord = 4000000


# def cov2(sx, sy, bx, by):
#     d = abs(bx - sx) + abs(by - sy)
#     for x in range(sx - d, sx + d + 1):
#         for y in range(sy - d, sy + d + 1):
#             if (
#                 abs(x - sx) + abs(y - sy) <= d
#                 and 0 <= x < max_coord
#                 and 0 <= y < max_coord
#             ):
#                 yield x, y


# coverage = set()
# for sx, sy, bx, by in sensors:
#     coverage.update(cov2(sx, sy, bx, by))


# def cov(sx, sy, bx, by, test_y):
#     width = abs(bx - sx) + abs(by - sy) - abs(test_y - sy)
#     return (x for x in range(sx - width, sx + width) if 0 <= x < max_coord)


for y in range(0, max_coord):
    ranges = sorted(
        [sx - width, sx + width]
        for sx, sy, bx, by in sensors
        if ((width := (abs(bx - sx) + abs(by - sy)) - abs(y - sy)) > 0)
    )

    ranges.sort()
    # combine overlapping ranges
    i = 0
    while i < len(ranges) - 1:
        left, right = ranges[i], ranges[i + 1]
        if left[1] + 1 >= right[0]:
            left[1] = max(right[1], left[1])
            ranges.pop(i + 1)
            continue
        i += 1
    # for range, next_range in zip(ranges, ranges[1:]):
    #     if range[1] + 1 >= next_range[0]:
    #         print(range, next_range)
    #         range[1] = max(next_range[1], range[1])
    #         ranges.remove(next_range)

    for l, r in ranges:
        if l <= 0 and r >= max_coord:
            break
        print((r + 1) * 4000000 + y)
        break

    # if len(ranges) == 1:
    #     continue

    # if any(l > 0 and r  max_coord for l,rin ranges):
    # if l <= 0 and r >= max_coord:
    #         break

    # print(ranges)
    # print((ranges[0][1] + 1) * max_coord + y)

    # if len(coverage) == max_coord:
    #     continue
    # for x in range(0, max_coord):
    #     if (x, y) not in coverage:
    #         print(x * 4000000 + y)
    #         exit()


# def cov2(sx, sy, bx, by):
#     d = abs(bx - sx) + abs(by - sy)
#     for x in range(0, max_coord):
#         for y in range(0, max_coord):
#             if abs(x - sx) + abs(y - sy) <= d:
#                 yield x, y


# cov = [[True for x in range(0, max_coord)] for y in range(0, max_coord)]
# print(len(cov))

# for sx, sy, bx, by in sensors:
#     full.difference_update(cov2(sx, sy, bx, by))

# print(len(full))

# x, y = full.pop()
# print(x * 4000000 + y)
