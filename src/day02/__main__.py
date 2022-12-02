from pathlib import Path

data = open(Path(__file__).with_name("input.txt")).read()
# data = "A Y\nB X\nC Z"

game_results = {
    "A X": 3 + 1,  # rock / rock
    "A Y": 6 + 2,  # rock / paper
    "A Z": 0 + 3,  # rock / scissors
    "B X": 0 + 1,  # paper / rock
    "B Y": 3 + 2,  # paper / paper
    "B Z": 6 + 3,  # paper / scissors
    "C X": 6 + 1,  # scissors / rock
    "C Y": 0 + 2,  # scissors / paper
    "C Z": 3 + 3,  # scissors / scissors
}

print(sum(game_results[game] for game in data.splitlines()))

game2_results = {
    "A X": 0 + 3,  # rock / lose (scissors)
    "A Y": 3 + 1,  # rock / draw (rock)
    "A Z": 6 + 2,  # rock / win (paper)
    "B X": 0 + 1,  # paper / lose (rock)
    "B Y": 3 + 2,  # paper / draw (paper)
    "B Z": 6 + 3,  # paper / win (scissors)
    "C X": 0 + 2,  # scissors / lose (paper)
    "C Y": 3 + 3,  # scissors / draw (scissors)
    "C Z": 6 + 1,  # scissors / win (rock)
}
print(sum(game2_results[game] for game in data.splitlines()))
