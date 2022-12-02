import run from "aocrunner";
import _ from "lodash";

const part1 = (rawInput: string): number =>
  _.sum(rawInput.split(/\n/).map((g) => {
    const theirs = g.charCodeAt(0) - 64, mine = g.charCodeAt(2) - 87
    return mine + [3, 0, 6][(theirs - mine + 3) % 3]
  }))

const part2 = (rawInput: string): number =>
  _.sum(rawInput.split(/\n/).map((g) => {
    const theirs = g.charCodeAt(0) - 64, ldw = g.charCodeAt(2) - 87
    return 1 + (ldw + theirs) % 3 + [0, 3, 6][ldw - 1]
  }))

run({
  part1: { solution: part1, tests: [{ input: "A Y\nB X\nC Z", expected: 15, },], },
  part2: { solution: part2, tests: [{ input: "A Y\nB X\nC Z", expected: 12, },], },
  trimTestInputs: true,
  // onlyTests: true,
});