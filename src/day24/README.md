# 🎄 Advent of Code 2022 - day 24 🎄

## Info

Task description: [link](https://adventofcode.com/2022/day/24)

## Notes
Nice cyclical pre-computation of blizzards, then started recursive finding but inevitably went djik-vibes.

Similar feeling to previous questions, but the wall-wrapping caused an annoying off-by-one error which meant I kept getting a too-low answer for the real input - turns out I was walking through the lower wall.

Part 2 nice and easy, just reset the queues once reached the end, and it auto-back-tracks.