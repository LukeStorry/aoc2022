use std::env;
mod day01;
// mod day02;
// mod day03;
// mod day04;
// mod day05;
// mod day06;
// mod day07;
// mod day08;
// mod day09;

fn main() {
    let day = env::args().nth(1).unwrap_or("all".to_string());

    match day.as_str() {
        "1" => day01::main(),
        // "2" => day02::solve(),
        // "3" => day03::solve(),
        // "4" => day04::solve(),
        // "5" => day05::solve(),
        // "6" => day06::solve(),
        // "7" => day07::solve(),
        // "8" => day08::solve(),
        // "9" => day09::solve(),
        // "10" => day10::solve(),
        "all" => {
            day01::main();
            // day2::solve();
            // day3::solve();
            // day4::solve();
            // day5::solve();
            // day6::solve();
            // day7::solve();
            // day8::solve();
            // day9::solve();
            // day10::solve();
        }
        _ => println!("Nothing for this day"),
    }
}
