from dataclasses import dataclass
from math import lcm, prod
import re
from typing import Callable, ClassVar

DIGITS = re.compile(r"\d+")


@dataclass
class Monkey:
    test: int
    items: list[int]
    operation: Callable
    test: int
    throw_true: int
    throw_false: int
    inspections: int = 0
    lcm: ClassVar[int] = 1

    def __init__(self, input: str):
        _, items, operation, test, true, false = input.splitlines()
        self.items = [int(i) for i in DIGITS.findall(items)]
        self.operation = lambda old: eval(operation.split("=")[1])
        self.test = int(DIGITS.findall(test)[0])
        self.throw_true = int(DIGITS.findall(true)[0])
        self.throw_false = int(DIGITS.findall(false)[0])
        Monkey.lcm = lcm(Monkey.lcm, self.test)

    def turn(self, monkeys, part1: bool):
        while self.items:
            self.inspections += 1
            worry = self.operation(self.items.pop(0)) % self.lcm
            if part1:
                worry = worry // 3
            recipient = self.throw_true if worry % self.test == 0 else self.throw_false
            monkeys[recipient].items.append(worry)


data = open("./src/day11/input.txt").read()

monkeys = [Monkey(s) for s in data.split("\n\n")]
for round in range(20):
    for monkey in monkeys:
        monkey.turn(monkeys, True)
print(prod(sorted(m.inspections for m in monkeys)[-2:]))

monkeys = [Monkey(s) for s in data.split("\n\n")]
for round in range(10000):
    for monkey in monkeys:
        monkey.turn(monkeys, False)
print(prod(sorted(m.inspections for m in monkeys)[-2:]))
