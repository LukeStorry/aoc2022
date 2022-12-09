from dataclasses import dataclass
from unittest import TestCase


@dataclass
class XYZ:
    x: int
    y: int

    def one(self):
        pass


def solve(data: str):
    lines = [x for lines in data.splitlines() for x in lines.split(" ")]
    objs = [XYZ(0, 0) for _ in range(10)]
    return int(data)


TestCase().assertEqual(solve("0"), 0)
TestCase().assertEqual(solve("1"), 1)
TestCase().assertEqual(solve("1"), 2)

# print(solve(open("./src/day1X/input.txt").read()))
