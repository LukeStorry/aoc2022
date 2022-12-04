import run from "aocrunner";
import _ from "lodash";

const part1 = (rawInput: string) =>
  rawInput
    .split(/\n/)
    .map((line) => line.split(/[-,]/).map(Number))
    .filter(
      ([firstStart, firstEnd, secondStart, secondEnd]) =>
        (firstStart <= secondStart && firstEnd >= secondEnd) ||
        (secondStart <= firstStart && secondEnd >= firstEnd)
    ).length;

const part2 = (rawInput: string) =>
  rawInput
    .split(/\n/)
    .map((line) => line.split(/[-,]/).map(Number))
    .filter(
      ([firstStart, firstEnd, secondStart, secondEnd]) =>
        (firstStart <= secondStart && secondStart <= firstEnd) ||
        (secondStart <= firstStart && firstStart <= secondEnd) ||
        (firstStart <= secondEnd && secondEnd <= firstEnd) ||
        (secondStart <= firstEnd && firstEnd <= secondEnd)
    ).length;

run({
  part1: {
    tests: [
      {
        input: `2-4,6-8
                2-3,4-5
                5-7,7-9
                2-8,3-7
                6-6,4-6
                2-6,4-8`,
        expected: 2,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `2-4,6-8
        2-3,4-5
        5-7,7-9
        2-8,3-7
        6-6,4-6
        2-6,4-8`,
        expected: 4,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  // onlyTests: true,
});
