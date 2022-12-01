import run from "aocrunner";
import _ from "lodash";

const parseInput = (rawInput: string) => rawInput.split("\n\n").map((e) => _.sum(e.split("\n").map(Number)));

const part1 = (rawInput: string) => _.max(parseInput(rawInput));
const part2 = (rawInput: string) => _.sum(parseInput(rawInput).sort().slice(0, 3));

run({
  part1: {
    tests: [
      {
        input: `1000
                2000
                3000

                4000

                5000
                6000

                7000
                8000
                9000

                10000`,
        expected: 24000,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `1000
                2000
                3000

                4000

                5000
                6000

                7000
                8000
                9000

                10000`,
        expected: 45000,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  // onlyTests: true,
});
