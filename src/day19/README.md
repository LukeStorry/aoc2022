# 🎄 Advent of Code 2022 - day 19 🎄

## Info

Task description: [link](https://adventofcode.com/2022/day/19)

## Notes

Initially went down a route focussing on coming up with clever exit conditions, but accidentally went into a DFS, and somehow ended up branching off too many times and then over-pruning, couldn’t get the right answer, and things were a slow OOP hell-hole where minutes being part of state meant it wasn’t easily debuggable.

Had a break, did some real work.

Came back form scratch, moved to looping through the minutes, with a smaller queue of possible states. Decided to use tuples as the underlying state datatype for some extra speed, kept things simple with generating the queue, and was finally getting the correct answers.

Then, rather than optimise with clever exit conditions, I made sure the elements of the state-tuple were in an order such that that sorting the queue would make sense, just pick the top 10000 each minute, and somehow that worked,  ~10sec total runtime


Part 2 was just changing a number, incredibly my lazy optimisation seemed pretty well set.



Gave it a go with standard tuples over named tuples, runtime was 10x faster, but code not even slightly readable.