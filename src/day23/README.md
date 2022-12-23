# 🎄 Advent of Code 2022 - day 23 🎄

## Info

Task description: [link](https://adventofcode.com/2022/day/23)

## Notes
Another fun one!

Very similar grid stuff to previous days, I’m in the groove of using sets of complex numbers to handle coordinates, so I did that again today.

Part2 was just time. Optimised a bit, then kicked it off in the background whilst I tried further improvements. Got it down to 8 minutes runtime, which I’m not too happy about but I’ve optimised as much as I can for this early in the morning.

Interestingly, one of my tries was to change to using integer x-y tuples and it was significantly slower, there’s a lot of accessing&checking so halving the memory accesses and only checking a complex number equality makes sense to be quicker.