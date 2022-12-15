import re


def part1(input: str, y=2000000):
    sensors = [
        [int(x) for x in re.findall(r"-?\d+", line)] for line in input.splitlines()
    ]

    return len(
        set(
            x
            for sensor_x, sensor_y, beacon_x, beacon_y in sensors
            if ((distance := abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)))
            for x in range(sensor_x - distance, sensor_x + distance + 1)
            if ((abs(x - sensor_x) + abs(y - sensor_y)) <= distance)
        )
        - set(beacon_x for _, _, beacon_x, beacon_y in sensors if beacon_y == y)
    )


def part2(data, max_coord=4000000):
    sensors = [
        [int(x) for x in re.findall(r"-?\d+", line)] for line in data.splitlines()
    ]
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
        start, end = ranges[0]
        while len(ranges) > 1 and end + 1 >= ranges[1][0]:
            end = max(end, ranges[1][1])
            ranges.pop(1)

        if ranges and start <= 0 and end <= max_coord:
            return (end + 1) * 4000000 + y


real_data = open("./src/day15/input.txt").read()
test_data = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15\nSensor at x=9, y=16: closest beacon is at x=10, y=16\nSensor at x=13, y=2: closest beacon is at x=15, y=3\nSensor at x=12, y=14: closest beacon is at x=10, y=16\nSensor at x=10, y=20: closest beacon is at x=10, y=16\nSensor at x=14, y=17: closest beacon is at x=10, y=16\nSensor at x=8, y=7: closest beacon is at x=2, y=10\nSensor at x=2, y=0: closest beacon is at x=2, y=10\nSensor at x=0, y=11: closest beacon is at x=2, y=10\nSensor at x=20, y=14: closest beacon is at x=25, y=17\nSensor at x=17, y=20: closest beacon is at x=21, y=22\nSensor at x=16, y=7: closest beacon is at x=15, y=3\nSensor at x=14, y=3: closest beacon is at x=15, y=3\nSensor at x=20, y=1: closest beacon is at x=15, y=3"


# part1_test = part1(test_data, y=10)
# print(part1_test)
# assert part1_test == 26

# part2_test = part2(test_data, max_coord=20)
# print(part2_test)
# assert part2_test == 56000011

part1_real = part1(real_data)
print(part1_real)
assert part1_real == 5144286

part2_real = part2(real_data)
print(part2_real)
assert part2_real == 10229191267339
