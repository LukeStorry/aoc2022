import run from "aocrunner";
import _ from "lodash";
const { isNumber, isArray, isNil } = _

type T = undefined[] | (number | T)[]

const parse = (input: string): T[][] =>
  input.split('\n\n').map(pair => pair.split('\n').map(eval));

const compare = (a: T, b: T, i = 0): boolean | undefined => {
  const left = a[i], right = b[i]

  if (isNil(left) || isNil(right)) {
    if (!isNil(right)) return true
    if (!isNil(left)) return false
    return undefined // backtrack
  }
  if (left === right) return compare(a, b, i + 1)
  if (isNumber(left) && isNumber(right)) return left < right
  if (isArray(left) && isArray(right)) return compare(left, right) ?? compare(a, b, i + 1)

  if (isArray(left)) return compare(left, [right]) ?? compare(a, b, i + 1)
  if (isArray(right)) return compare([left], right) ?? compare(a, b, i + 1)
  return false
}


const part1 = (input: string): number => parse(input)
  .reduce(((prev, [a, b], pair_index) => compare(a, b) ? prev + (pair_index + 1) : prev), 0)

const new_pair: T[] = [[2], [[6]]]
const part2 = (input: string) => parse(input)
  .flatMap(p => p).concat(new_pair)
  .sort(((a, b) => compare(a, b) ? -1 : 1))
  .reduce((r, p, i) => new_pair.includes(p) ? r * (i + 1) : r, 1)

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
  part2: {
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
        expected: 140
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  // onlyTests: true,
});
