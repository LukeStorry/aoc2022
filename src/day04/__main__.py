import re

data = open("./src/day04/input.txt").read()


def v1():
    overlaps = 0
    contains = 0

    for pair in data.splitlines():
        [a, b, c, d] = map(int, re.split("[-,]", pair))
        if (a <= c and b >= d) or (c <= a and d >= b):
            contains += 1
        if (a <= c <= b) or (c <= a <= d) or (a <= d <= b) or (c <= b <= d):
            overlaps += 1

    return (contains, overlaps)


def v2():
    pairs = [list(map(int, re.split("[-,]", pair))) for pair in data.splitlines()]
    return (
        sum(
            1 if (a <= c and b >= d) or (c <= a and d >= b) else 0
            for [a, b, c, d] in pairs
        ),
        sum(
            1 if (a <= c <= b) or (c <= a <= d) or (a <= d <= b) or (c <= b <= d) else 0
            for [a, b, c, d] in pairs
        ),
    )


print(v1())
print(v2())
