import re

data = open("./src/day15/input.txt").read()
sensors = [[int(x) for x in re.findall(r"-?\d+", line)] for line in data.splitlines()]

# Part 1
y = 2000000

part1 = len(
    set(
        x
        for sensor_x, sensor_y, beacon_x, beacon_y in sensors
        if ((distance := abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)))
        for x in range(sensor_x - distance, sensor_x + distance + 1)
        if ((abs(x - sensor_x) + abs(y - sensor_y)) <= distance)
    )
    - set(beacon_x for _, _, beacon_x, beacon_y in sensors if beacon_y == y)
)
print(part1)

assert part1 == 5144286


# Part 2
max_coord = 4000000

for y in range(0, max_coord):
    ranges = sorted(
        [sensor_x - width, sensor_x + width]
        for sensor_x, sensor_y, beacon_x, beacon_y in sensors
        if (
            (distance := abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y))
            and (width := distance - abs(y - sensor_y)) > 0
        )
    )

    # combine overlapping ranges
    overlapping_range = ranges[0]
    while len(ranges) > 1 and overlapping_range[1] + 1 >= ranges[1][0]:
        overlapping_range[1] = max(overlapping_range[1], ranges[1][1])
        ranges.pop(1)

    if len(ranges) == 1 or any(l <= 0 and r >= max_coord for l, r in ranges):
        continue
    part2 = (ranges[1][0] - 1) * 4000000 + y
    break

print(part2)
assert part2 == 10229191267339
