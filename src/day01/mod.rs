use std::num::ParseIntError;

use aoc_runner_derive::{aoc, aoc_generator};

#[aoc_generator(day1)]
fn parse(input: &str) -> Result<Vec<u32>, ParseIntError> {
    input
        .split("\n\n")
        .map(|elf| elf.lines().map(str::parse::<u32>).sum())
        .collect()
}

#[aoc(day1, part1)]
fn part_1(data: &Vec<u32>) -> u32 {
    *data.iter().max().unwrap()
}

#[aoc(day1, part2)]
fn part_2(data: &Vec<u32>) -> u32 {
    let sorted = {
        let mut c: Vec<u32> = data.to_owned();
        c.sort_unstable();
        c
    };
    sorted.iter().rev().take(3).sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000";

    #[test]
    fn test_part_1() {
        let data = &parse(EXAMPLE).unwrap();
        assert_eq!(part_1(data), 24000);
    }
    #[test]
    fn test_part_2() {
        let data = &parse(EXAMPLE).unwrap();
        assert_eq!(part_2(data), 45000);
    }
}
