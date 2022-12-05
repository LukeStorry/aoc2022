use std::str::FromStr;

use aoc_runner_derive::{aoc, aoc_generator};
use itertools::Itertools;
use regex::Regex;

#[derive(Debug)]
struct Move(usize, usize, usize);
#[derive(Debug)]
struct Stack(Vec<char>);
#[derive(Debug)]
struct Stacks(Vec<Stack>);

impl FromIterator<Stack> for Stacks {
    fn from_iter<T: IntoIterator<Item = Stack>>(iter: T) -> Self {
        Self(iter.into_iter().collect())
    }
}

impl FromIterator<char> for Stack {
    fn from_iter<T: IntoIterator<Item = char>>(iter: T) -> Self {
        Self(iter.into_iter().collect())
    }
}

impl FromStr for Stacks {
    type Err = std::num::ParseIntError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let lines = s.lines().collect_vec();
        let vec = lines
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
            .collect();
        Ok(vec)
    }
}

struct Data {
    stack: Stack,
    moves: Vec<Move>,
}

fn parse_moves(s: &str) -> Vec<Move> {
    Regex::new(r"(\d+).*(\d+).*(\d+)")
        .unwrap()
        .captures_iter(s)
        .map(|cap| {
            Move(
                cap[1].parse().unwrap(),
                cap[2].parse().unwrap(),
                cap[3].parse().unwrap(),
            )
        })
        .collect()
}

#[aoc_generator(day5)]
fn parse(input: &str) -> (Stacks, Vec<Move>) {
    let (stack_lines, moves_lines) = input.split("\n\n").collect_tuple().unwrap();

    (
        Stacks::from_str(stack_lines).unwrap(),
        parse_moves(moves_lines),
    )
}

#[aoc(day5, part1)]
fn part_1((stacks, moves): &(Stacks, Vec<Move>)) -> &str {
    ""
}

#[aoc(day5, part2)]
fn part_2((stacks, moves): &(Stacks, Vec<Move>)) -> &str {
    ""
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str =  "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2";

    #[test]
    fn test_part_1() {
        let data = &parse(EXAMPLE);
        println!("{:?}", data);
        assert_eq!(1, 1);
    }
    #[test]
    fn test_part_2() {
        let data = &parse(EXAMPLE);
        // assert_eq!(part_2(data), 45000);
    }
}
