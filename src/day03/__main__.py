from pathlib import Path

data = open(Path(__file__).with_name("input.txt")).read()
# data = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"

lines = data.splitlines()
duplicates = [
    (set(rucksack[:half]) & set(rucksack[half:])).pop()
    for rucksack in lines
    if (half := len(rucksack) // 2)
]
print(sum(ord(d) - (96 if d.islower() else 38) for d in duplicates))

list_chunked = [
    (set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])).pop()
    for i in range(0, len(lines), 3)
]
print(sum(ord(d) - (96 if d.islower() else 38) for d in list_chunked))
