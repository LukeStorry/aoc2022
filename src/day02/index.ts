import run from "aocrunner";
import _ from "lodash";

const part1 = (rawInput: string): number =>
  _.sum(rawInput.split(/\n/).map((g) => {
    const theirs = g.charCodeAt(0) - 'A'.charCodeAt(0)
    const mine = g.charCodeAt(2) - 'X'.charCodeAt(0)
    const drawLoseWin = (theirs - mine + 3) % 3;
    return 1 + mine + [3, 0, 6][drawLoseWin]
  }))

const part2 = (rawInput: string): number =>
  _.sum(rawInput.split(/\n/).map((g) => {
    const theirs = g.charCodeAt(0) - 'A'.charCodeAt(0)
    const loseDrawWin = g.charCodeAt(2) - 'X'.charCodeAt(0)
    return 1 + (loseDrawWin + theirs + 2) % 3 + [0, 3, 6][loseDrawWin]
  }))

run({
  part1: { solution: part1, tests: [{ input: "A Y\nB X\nC Z", expected: 15 }] },
  part2: { solution: part2, tests: [{ input: "A Y\nB X\nC Z", expected: 12 }] },
  trimTestInputs: true,
  // onlyTests: true,
});