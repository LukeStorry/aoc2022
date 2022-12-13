import run from "aocrunner";
import _ from "lodash";

const parse = (input: string) =>
  input.split('\n\n').map(pair => pair.split('\n').map(eval));

const compare = (a, b, i): boolean | undefined => {
  const left = a[i], right = b[i]

  // end of list
  if (_.isNil(left) && _.isNil(right)) return undefined // backtrack
  if (_.isNil(left) && !_.isNil(right)) return true
  if (!_.isNil(left) && _.isNil(right)) return false

  if (left == right) return compare(a, b, i + 1)
  if (_.isNumber(left) && _.isNumber(right)) return left < right
  if (_.isArray(left) && _.isArray(right)) return compare(left, right, 0) ?? compare(a, b, i + 1)

  if (_.isArray(left)) return compare(left, [right], 0) ?? compare(a, b, i + 1)
  if (_.isArray(right)) return compare([left], right, 0) ?? compare(a, b, i + 1)
  return false
}


const part1 = (input: string): number => parse(input).reduce((
  (prev, [a, b], pair_index) => compare(a, b, 0) ? prev + (pair_index + 1) : prev), 0)
// const part1 = (input: string) => parse(input).forEach(([a, b], pair_index) => {
//   console.log(pair_index + 1, compare(a, b, 0));
// })

const part2 = (input: string) => parse(input);

run({
  part1: {
    tests: [
      {
        input: `[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]`,
        expected: 13,
      },
    ],
    solution: part1,
  },
  // part2: {
  //   tests: [
  //     {
  //       input: `

  //       `,
  //       expected: 0,
  //     },
  //   ],
  //   solution: part2,
  // },
  trimTestInputs: true,
  // onlyTests: true,
});
