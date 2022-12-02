import run from "aocrunner";
import _ from "lodash";

const part1 = (rawInput: string): number =>
  _.sum(rawInput.split(/\n/).map((g) => {
    const theirs = g.charCodeAt(0) - 64, mine = g.charCodeAt(2) - 87
    return mine + [3, 0, 6][(theirs - mine + 3) % 3]
  }))

const part2_results = new Map([
  ["A X", 0 + 3],  // rock / lose (scissors)
  ["A Y", 3 + 1],  // rock / draw (rock)
  ["A Z", 6 + 2],  // rock / win (paper)
  ["B X", 0 + 1],  // paper / lose (rock)
  ["B Y", 3 + 2],  // paper / draw (paper)
  ["B Z", 6 + 3],  // paper / win (scissors)
  ["C X", 0 + 2],  // scissors / lose (paper)
  ["C Y", 3 + 3],  // scissors / draw (scissors)
  ["C Z", 6 + 1],  // scissors / win (rock)
])

const part2 = (rawInput: string): number =>
  _.sum(rawInput.split(/\n/).map((g) => part2_results.get(g)))

run({
  part1: { solution: part1, tests: [{ input: "A Y\nB X\nC Z", expected: 15, },], },
  part2: { solution: part2, tests: [{ input: "A Y\nB X\nC Z", expected: 12, },], },
  trimTestInputs: true,
  // onlyTests: true,
});
