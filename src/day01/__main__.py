from pathlib import Path

data = open(Path(__file__).with_name("input.txt")).read()

elves_totals = sorted(sum(int(n) for n in e.split("\n")) 
                                 for e in data.split("\n\n"))
print(elves_totals[-1])
print(sum(elves_totals[-3:]))
