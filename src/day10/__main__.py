def solve(data: str):
    x = [1, 1]
    count = 0
    for cmd in data.splitlines():
        match cmd.split():
            case ["noop"]:
                x.append(x[-1])
            case ["addx", num]:
                x.append(x[-1])
                x.append(x[-1] + int(num))
            case _:
                print(f"unknown command {cmd}")

    # print([[i, x[i], i * x[i]] for i in (20, 60, 100, 140, 180, 220)])
    return sum(i * x[i] for i in (20, 60, 100, 140, 180, 220))


# solve("noop\naddx 3\naddx -5\n")
print(solve(open("./src/day10/example.txt").read()))
print(solve(open("./src/day10/input.txt").read()))
