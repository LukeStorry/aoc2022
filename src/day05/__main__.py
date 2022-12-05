import re

data = open("./src/day05/input.txt").read()
# data = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"


stack_lines, moves_lines = [d.splitlines() for d in data.split("\n\n")]
n_stacks = int(stack_lines[-1][-2])
moves = [[int(x) for x in re.findall(r"\d+", move)] for move in moves_lines]
stacks = [
    [x for line in reversed(stack_lines) if ((x := line[1 + n * 4]) and x.isalpha())]
    for n in range(n_stacks)
]

for [num, frm, to] in moves:
    for _ in range(num):
        stacks[to - 1].append(stacks[frm - 1].pop())

print("".join(s[-1] for s in stacks))


stacks = [
    [x for line in reversed(stack_lines) if ((x := line[1 + n * 4]) and x.isalpha())]
    for n in range(n_stacks)
]
for [num, frm, to] in moves:
    from_stack = stacks[frm - 1]
    stacks[to - 1].extend(from_stack[-num:])
    del from_stack[-num:]

print("".join(s[-1] for s in stacks))
