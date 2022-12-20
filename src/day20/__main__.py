def mix(coordinates: list[int], times=1):
    coords = list(enumerate(coordinates))
    for _ in range(times):
        for e in enumerate(coordinates):
            index = coords.index(e)
            _, val = coords.pop(index)
            new_index = (index + val) % len(coords)
            coords = coords[:new_index] + [e] + coords[new_index:]
    return [x for _, x in coords]


file = [int(n) for n in open("./src/day20/input.txt").read().splitlines()]
mixed = mix(file)
print(sum(mixed[(mixed.index(0) + i) % len(mixed)] for i in (1000, 2000, 3000)))

mixed = mix([n * 811589153 for n in file], 10)
print(sum(mixed[(mixed.index(0) + i) % len(mixed)] for i in (1000, 2000, 3000)))
