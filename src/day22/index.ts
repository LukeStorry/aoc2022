import run from "aocrunner";
import _ from "lodash";

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => parseInput(rawInput);
const part2 = (rawInput: string) => parseInput(rawInput);

run({
  part1: {
    tests: [
      {
        input: `
        
        `,
        expected: 0,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
        
        `,
        expected: 0,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: true,
});
