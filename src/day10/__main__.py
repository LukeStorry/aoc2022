data = open("./src/day10/input.txt").read()

reg_x = [1, 1]
count = 0
for cmd in data.splitlines():
    match cmd.split():
        case ["noop"]:
            reg_x.append(reg_x[-1])
        case ["addx", num]:
            reg_x.append(reg_x[-1])
            reg_x.append(reg_x[-1] + int(num))

print(sum(i * reg_x[i] for i in (20, 60, 100, 140, 180, 220)))

for row in range(6):
    for col in range(40):
        sprite = reg_x[row * 40 + col + 1]
        print("#" if col in (sprite - 1, sprite, sprite + 1) else ".", end="")
    print()
