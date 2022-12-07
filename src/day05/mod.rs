use aoc_runner_derive::aoc;
use itertools::Itertools;
use regex::Regex;

pub trait FromStr {
    fn from_str(s: &str) -> Self;
}

type Moves = Vec<(usize, usize, usize)>;
type Stack = Vec<char>;
type Stacks = Vec<Stack>;
type Data = (Stacks, Moves);

impl FromStr for Stacks {
    fn from_str(s: &str) -> Self {
        let lines = s.lines().collect_vec();
        lines
            .last()
            .unwrap()
            .chars()
            .enumerate()
            .filter(|(_, c)| c.is_numeric())
            .map(|(stack_index, c)| {
                lines
                    .iter()
                    .map(|line| line.chars().nth(stack_index).unwrap())
                    .filter(|char| char.is_alphabetic())
                    .collect()
            })
            .collect()
    }
}

impl FromStr for Moves {
    fn from_str(s: &str) -> Self {
        Regex::new(r"(\d+).*(\d+).*(\d+)")
            .unwrap()
            .captures_iter(s)
            .map(|cap| {
                (
                    cap[1].parse().unwrap(),
                    cap[2].parse().unwrap(),
                    cap[3].parse().unwrap(),
                )
            })
            .collect()
    }
}

impl FromStr for Data {
    fn from_str(s: &str) -> Self {
        let (stack_lines, moves_lines) = s.split("\n\n").collect_tuple().unwrap();
        (Stacks::from_str(stack_lines), Moves::from_str(moves_lines))
    }
}

fn part_1(input: &str) -> &str {
    let (mut stacks, moves) = Data::from_str(input);

    for (from, to, amount) in moves {
        let from_stack = stacks.get_mut(from - 1).unwrap();
        let to_stack = stacks.get_mut(to - 1).unwrap();

        for _ in 0..amount {
            let disk = from_stack.pop().unwrap();
            to_stack.push(disk);
        }
    }
}

fn part_2(input: &str) -> &str {
    ""
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str =  "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2";

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(EXAMPLE), "CMZ");
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(EXAMPLE), "CMZ");
    }
}
