from dataclasses import dataclass
import re

DIGITS = re.compile(r"\d+")


@dataclass
class XYZ:
    x: int
    y: int

    def one(self, s):
        d = int(DIGITS.findall(s)[0])


data = open("./src/day1x/input.txt").read()


lines = [x for lines in data.splitlines() for x in lines.split(" ")]
objs = [XYZ(0, 0) for _ in range(10)]
