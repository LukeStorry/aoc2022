from random import random
import re

input = open("./src/day21/input.txt").read()
exec(re.sub(r"\(\)(\w+)", r"\1()", input.replace(": ", "=lambda:").replace(" ", "()")))
print(int(root()))

root_1, root_2 = [eval("lambda: " + x + "()") for x in re.findall(r"root: (\w+) . (\w+)", input)[0]]
estimates = []
for _ in range(100):
    try_1, try_2 = random() * 1000000, random() * 100000000
    humn = lambda: try_1
    result_1 = root_1() - root_2()
    humn = lambda: try_2
    result_2 = root_1() - root_2()
    estimates.append((try_1 * result_2 - try_2 * result_1) / (result_2 - result_1))
estimate = int(sum(estimates) / len(estimates))

for x in range(estimate - 1000, estimate + 1000):
    humn = lambda: x
    if root_1() == root_2():
        print(x)
        break
