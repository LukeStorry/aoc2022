# Day 17: Pyroclastic Flow

<em>How many units tall will the tower of rocks be after 2022 rocks have stopped falling?</em>

[Full Question](https://adventofcode.com/2022/day/17)

## Notes
A tough but quite fun one I think.
Original attempt got stuck in edge-cases of when rocks overlap, but I really didn't want a grid so doubled-down on the sets of coordinates with an array of max-heights, which worked well.

Part 2 just being a really big number made me groan a bit. I tried a dumb naive attempt at finding some simple cycles, using the max-heights array I already had, not expecting there to be any (or for it to be correct), but then it worked! :shrug::smile: