use aoc_runner_derive::aoc;

#[aoc(day2, part1, match)]
fn part_1(input: &str) -> u16 {
    input
        .lines()
        .map(|line| match line {
            "A X" => 3 + 1, // rock / rock
            "A Y" => 6 + 2, // rock / paper
            "A Z" => 0 + 3, // rock / scissors
            "B X" => 0 + 1, // paper / rock
            "B Y" => 3 + 2, // paper / paper
            "B Z" => 6 + 3, // paper / scissors
            "C X" => 6 + 1, // scissors / rock
            "C Y" => 0 + 2, // scissors / paper
            "C Z" => 3 + 3, // scissors / scissors
            &_ => panic!("unknown game"),
        })
        .sum()
}
#[aoc(day2, part1, modulo)]
fn part_1_mod(input: &str) -> u16 {
    input
        .lines()
        .map(|line| {
            let (theirs, mine) = (
                line.chars().next().unwrap() as u16 - 64,
                line.chars().last().unwrap() as u16 - 87,
            );
            mine + [3, 0, 6][((theirs + 3 - mine) % 3) as usize]
        })
        .sum()
}
#[aoc(day2, part2, match)]
fn part_2(input: &str) -> u16 {
    input
        .lines()
        .map(|line| match line {
            "A X" => 0 + 3, // rock / lose (scissors)
            "A Y" => 3 + 1, // rock / draw (rock)
            "A Z" => 6 + 2, // rock / win (paper)
            "B X" => 0 + 1, // paper / lose (rock)
            "B Y" => 3 + 2, // paper / draw (paper)
            "B Z" => 6 + 3, // paper / win (scissors)
            "C X" => 0 + 2, // scissors / lose (paper)
            "C Y" => 3 + 3, // scissors / draw (scissors)
            "C Z" => 6 + 1, // scissors / win (rock)
            &_ => panic!("unknown game"),
        })
        .sum()
}
#[aoc(day2, part2, modulo)]
fn part_2_mod(input: &str) -> u16 {
    input
        .lines()
        .map(|line| {
            let (theirs, lose_draw_win) = (
                line.chars().next().unwrap() as u16 - 64,
                line.chars().last().unwrap() as u16 - 87,
            );
            1 + (lose_draw_win + theirs) % 3 + [0, 3, 6][lose_draw_win as usize - 1]
        })
        .sum()
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1("A Y\nB X\nC Z"), 15);
    }
    #[test]
    fn test_part_1_mod() {
        assert_eq!(part_1_mod("A Y\nB X\nC Z"), 15);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2("A Y\nB X\nC Z"), 12);
    }
    #[test]
    fn test_part_2_mod() {
        assert_eq!(part_2_mod("A Y\nB X\nC Z"), 12);
    }
}
