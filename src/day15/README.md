# Day 15: Beacon Exclusion Zone

Consult the report from the sensors you just deployed. <em>In the row where <code>y=2000000</code>, how many positions cannot contain a beacon?</em>

[Full Question](https://adventofcode.com/2022/day/15)

## Notes
Part 1 was ok, did my normal approach of using a set of coordinates to find the amount on a single row.

But then part 2 was way to big for set operations, so after trying various ways I eventually  got a range-generation-and-combination loop thing working: