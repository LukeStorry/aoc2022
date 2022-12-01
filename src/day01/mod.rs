use itertools::Itertools;
use std::fs::read_to_string;

fn parse(input: &str) -> Vec<u32> {
    input
        .split("\n\n")
        .map(|elf| elf.lines().map(|i| i.parse::<u32>().unwrap()).sum())
        .collect()
}

fn part_1(input: &str) -> u32 {
    *parse(input).iter().max().unwrap()
}

fn part_2(input: &str) -> u32 {
    parse(input).into_iter().sorted().rev().take(3).sum()
}

pub fn main() {
    let input = read_to_string("src/day01/input.txt").unwrap();
    print!("Day 01 part 1: {}\n", part_1(&input));
    print!("Day 01 part 2: {}\n", part_2(&input));
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_part_1() {
        let input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000";
        assert_eq!(part_1(&input), 24000);
    }
    #[test]
    fn test_part_2() {
        let input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000";
        assert_eq!(part_2(&input), 45000);
    }
}
