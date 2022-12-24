# Day 20: Grove Positioning System

Mix your encrypted file exactly once. <em>What is the sum of the three numbers that form the grove coordinates?</em>

[Full Question](https://adventofcode.com/2022/day/20)

## Notes

Should have been simple.
Few fun issues meant I nearly missed my train this morning.
Turns out python's `list.insert()` won't append, needs to be special cased for those wraparounds, so did basic string concatenation instead.
And of course the input has duplicates, took me far to long to figure out I couldn't do the `indexOf()` thing, but enumerating the list first to make elements unique tuples sorted it right out.