data = open("./src/day06/input.txt").read()

iter = enumerate(zip(data, data[1:], data[2:], data[3:]), 4)
print(next(i for i, message in iter if len(set(message)) == 4))

iter = enumerate(zip(*(data[i:] for i in range(14))), 14)
print(next(i for i, message in iter if len(set(message)) == 14))
