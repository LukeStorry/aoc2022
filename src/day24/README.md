# Day 24: Blizzard Basin

<em>What is the fewest number of minutes required to avoid the blizzards and reach the goal?</em>

[Full Question](https://adventofcode.com/2022/day/24)

## Notes
Nice cyclical pre-computation of blizzards, then started recursive finding but inevitably went djik-vibes.

Similar feeling to previous questions, but the wall-wrapping caused an annoying off-by-one error which meant I kept getting a too-low answer for the real input - turns out I was walking through the lower wall.

Part 2 nice and easy, just reset the queues once reached the end, and it auto-back-tracks.