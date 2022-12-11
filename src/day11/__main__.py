from dataclasses import dataclass
from math import prod


@dataclass
class Monkey:
    test: int
    items: list
    operation: str
    test: int
    true_recipient: int
    false_recipient: int
    inspections: int = 0

    def __init__(self, input: str):
        id, items, operation, test, true, false = input.splitlines()
        self.id = int(id[-2])
        self.items = [int(i) for i in items.split(":")[1].split(", ")]
        self.operation = operation.split("= ")[1]
        self.test = int(test.split(" ")[-1])
        self.true_recipient = int(true[-1])
        self.false_recipient = int(false[-1])

    def turn(self, monkeys):
        while self.items:
            self.inspections += 1
            old = self.items.pop(0)
            worry = eval(self.operation) // 3
            recipient = (
                self.true_recipient if worry % self.test == 0 else self.false_recipient
            )
            monkeys[recipient].items.append(worry)


data = open("./src/day11/input.txt").read()
monkeys = [Monkey(s) for s in data.split("\n\n")]

for _ in range(20):
    for monkey in monkeys:
        monkey.turn(monkeys)

print(prod(sorted(m.inspections for m in monkeys)[-2:]))
