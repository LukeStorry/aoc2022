from random import random
import re

input = open("./src/day21/input.txt").read()
exec(re.sub(r"\(\)(\w+)", r"\1()", input.replace(": ", "=lambda:").replace(" ", "()")))
print(int(root()))

root_nodes = [x + "()" for x in re.findall(r"root: (\w+) . (\w+)", input)[0]]
root = lambda: eval("==".join(root_nodes))

estimates = []
for _ in range(1000):
    x1, x2 = random() * 10000, random() * 100000
    humn = lambda: x1
    y1 = eval(root_nodes[0]) - eval(root_nodes[1])
    humn = lambda: x2
    y2 = eval(root_nodes[0]) - eval(root_nodes[1])
    estimates.append((x1 * y2 - x2 * y1) / (y2 - y1))

avg = int(sum(estimates) / len(estimates))

for x in range(avg - 10000, avg + 10000):
    humn = lambda: x
    if root():
        print(x)
        break

# 3272260914328
