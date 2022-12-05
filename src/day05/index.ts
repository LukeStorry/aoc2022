import run from "aocrunner";

type Data = {
  moves: { from: number; to: number; amount: number }[];
  stacks: string[][];
};

const parseInput = (rawInput: string): Data => {
  const [stackLines, movesLines] = rawInput.split(/\n\n/);
  const n_stacks = Number(stackLines[stackLines.length - 2]);
  return {
    stacks: Array.from(stackLines.matchAll(/\[([A-Z])\]/g)).reduce(
      (acc, match) => {
        const stack_num = ((match.index! / 4) % n_stacks) + 1;
        acc[stack_num] = [match[1], ...(acc[stack_num] || [])];
        return acc;
      },
      [[""]]
    ),

    moves: movesLines
      .split(/\n/)
      .map((move) => move.match(/\d+/g)!.map(Number))
      .map(([amount, from, to]) => ({ amount, from, to })),
  };
};

const part1 = ({ stacks, moves }: Data) => {
  moves.forEach(({ from, to, amount }) =>
    stacks[from]
      .splice(-amount)
      .reverse()
      .forEach((n) => stacks[to].push(n))
  );
  return stacks.map((s) => s.at(-1)).join("");
};

const part2 = ({ stacks, moves }: Data) => {
  moves.forEach(({ from, to, amount }) =>
    stacks[from]
      .splice(-amount)
      .forEach((n) => stacks[to].push(n))
  );
  return stacks.map((s) => s.at(-1)).join("");
};

run({
  part1: {
    tests: [
      {
        input:
          "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2",
        expected: "CMZ",
      },
    ],
    solution: (i) => part1(parseInput(i)),
  },
  part2: {
    tests: [
      {
        input:
          "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2",
        expected: "MCD",
      },
    ],
    solution: (i) => part2(parseInput(i)),
  },
  trimTestInputs: true,
  // onlyTests: true,
});
