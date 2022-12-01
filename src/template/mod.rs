use std::num::ParseIntError;

use aoc_runner_derive::{aoc, aoc_generator};

#[aoc_generator(dayX)]
fn parse(input: &str) -> Result<Vec<u32>, ParseIntError> {
    input.split("\n").collect()
}

#[aoc(dayX, part1)]
fn part_1(data: &Vec<u32>) -> u32 {
    0
}

#[aoc(dayX, part2)]
fn part_2(data: &Vec<u32>) -> u32 {
    0
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = "";

    #[test]
    fn test_part_1() {
        let data = &parse(EXAMPLE).unwrap();
        assert_eq!(part_1(data), 0);
    }
    #[test]
    fn test_part_2() {
        let data = &parse(EXAMPLE).unwrap();
        assert_eq!(part_2(data), 0);
    }
}
