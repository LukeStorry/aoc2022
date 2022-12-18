# 🎄 Advent of Code 2022 - day 18 🎄

## Info

Task description: [link](https://adventofcode.com/2022/day/18)

## Notes
Good fun, part 1 was asking for a one-liner:
```python
print(
    sum(
        len(set((x + dx, y + dy, z + dz) for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))) - cubes)
        for x, y, z in cubes
        if (cubes := set((int(x), int(y), int(z)) for x, y, z in re.findall(r"(\d+),(\d+),(\d+)", open("./src/day18/input.txt").read())))
    )
)
```


Then part2 was a touch fiddly but a simple djik-style search did it nicely, much easier than the past few days have been