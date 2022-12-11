from dataclasses import dataclass
from math import lcm, prod
import re
from typing import Callable


@dataclass
class Monkey:
    test: int
    items: list
    operation: Callable
    test: int
    true: int
    false: int
    inspections: int = 0

    def __init__(self, input: str):
        _, items, operation, test, true, false = input.splitlines()
        self.items = [int(i) for i in re.findall(r"\d+", items)]
        self.test = int(test.split("divisible by")[1])
        self.true, self.false = int(true[-1]), int(false[-1])

        match operation.split("= old ")[1].split():
            case ["*", "old"]:
                self.operation = lambda old: old * old
            case ["*", num]:
                self.operation = lambda old, num=num: old * int(num)
            case ["+", num]:
                self.operation = lambda old, num=num: old + int(num)

    def turn(self, monkeys, lcm=None):
        while self.items:
            self.inspections += 1
            worry = self.operation(self.items.pop(0))
            if lcm:
                worry = worry % lcm
            else:
                worry = worry // 3
            recipient = self.true if worry % self.test == 0 else self.false
            monkeys[recipient].items.append(worry)


data = open("./src/day11/input.txt").read()

monkeys = [Monkey(s) for s in data.split("\n\n")]
for round in range(20):
    for monkey in monkeys:
        monkey.turn(monkeys)
print(prod(sorted(m.inspections for m in monkeys)[-2:]))

monkeys = [Monkey(s) for s in data.split("\n\n")]
lcm = lcm(*[m.test for m in monkeys])
for round in range(10000):
    for monkey in monkeys:
        monkey.turn(monkeys, lcm)
print(prod(sorted(m.inspections for m in monkeys)[-2:]))
