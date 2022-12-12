import run from "aocrunner";
import aStar from 'a-star';

type Node = { x: number, y: number, c: string }

const setup = (input: string) => {
  const nodes: Node[][] = input.split('\n')
    .map((row, y) => row.split('')
      .map((c, x) => ({ x, y, c })));
  return {
    nodes,
    start: nodes.flatMap(n => n).find(({ c }) => c == 'E')!,
    neighbor: ({ x, y, c }: Node) =>
      [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        .flatMap(([new_x, new_y]) => nodes[new_y]?.[new_x] || [])
        .filter(({ c: new_c }) => {
          if (c == 'E') return new_c == 'z'
          if (c == 'a' && new_c == 'S') return true
          return c.charCodeAt(0) - new_c.charCodeAt(0) <= 1;
        }),
    hash: ({ x, y, c }: Node) => `${x}${y}${c}`,
    heuristic: ({ c }: Node) => c.charCodeAt(0) - 'a'.charCodeAt(0) + 10000,
    distance: () => 1
  }
}

const part1 = (input: string) => aStar({ ...setup(input), isEnd: ({ c }: Node) => c == 'S', }).cost
const part2 = (input: string) => aStar({ ...setup(input), isEnd: ({ c }: Node) => c == 'a', }).cost

run({
  part1: {
    tests: [
      {
        input: `Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi`,
        expected: 31,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi`,
        expected: 29,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  // onlyTests: true,
});
