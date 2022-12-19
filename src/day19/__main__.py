from collections import namedtuple
from math import prod
import re

State = namedtuple("State", "geode geode_robots obsidian obsidian_robots clay clay_robots ore ore_robots")
Blueprint = namedtuple("State", "id ore_ore clay_ore obsidian_ore obsidian_clay geode_ore geode_obsidian")


def most_geodes(blueprint: Blueprint, until: int):
    queue = [State(0, 0, 0, 0, 0, 0, 0, 1)]
    for _ in range(0, until):
        queue = set(
            new_state
            for state in sorted(queue)[-10000:]
            for condition, new_state in (
                (
                    True,
                    State(
                        ore=state.ore + state.ore_robots,
                        clay=state.clay + state.clay_robots,
                        obsidian=state.obsidian + state.obsidian_robots,
                        geode=state.geode + state.geode_robots,
                        ore_robots=state.ore_robots,
                        clay_robots=state.clay_robots,
                        obsidian_robots=state.obsidian_robots,
                        geode_robots=state.geode_robots,
                    ),
                ),
                (
                    blueprint.ore_ore <= state.ore,
                    State(
                        ore_robots=state.ore_robots + 1,
                        ore=state.ore + state.ore_robots - blueprint.ore_ore,
                        clay=state.clay + state.clay_robots,
                        obsidian=state.obsidian + state.obsidian_robots,
                        geode=state.geode + state.geode_robots,
                        clay_robots=state.clay_robots,
                        obsidian_robots=state.obsidian_robots,
                        geode_robots=state.geode_robots,
                    ),
                ),
                (
                    blueprint.clay_ore <= state.ore,
                    State(
                        clay_robots=state.clay_robots + 1,
                        ore=state.ore + state.ore_robots - blueprint.clay_ore,
                        clay=state.clay + state.clay_robots,
                        obsidian=state.obsidian + state.obsidian_robots,
                        geode=state.geode + state.geode_robots,
                        ore_robots=state.ore_robots,
                        obsidian_robots=state.obsidian_robots,
                        geode_robots=state.geode_robots,
                    ),
                ),
                (
                    blueprint.obsidian_ore <= state.ore and blueprint.obsidian_clay <= state.clay,
                    State(
                        obsidian_robots=state.obsidian_robots + 1,
                        ore=state.ore + state.ore_robots - blueprint.obsidian_ore,
                        clay=state.clay + state.clay_robots - blueprint.obsidian_clay,
                        obsidian=state.obsidian + state.obsidian_robots,
                        geode=state.geode + state.geode_robots,
                        ore_robots=state.ore_robots,
                        clay_robots=state.clay_robots,
                        geode_robots=state.geode_robots,
                    ),
                ),
                (
                    blueprint.geode_ore <= state.ore and blueprint.geode_obsidian <= state.obsidian,
                    State(
                        geode_robots=state.geode_robots + 1,
                        ore=state.ore + state.ore_robots - blueprint.geode_ore,
                        obsidian=state.obsidian + state.obsidian_robots - blueprint.geode_obsidian,
                        clay=state.clay + state.clay_robots,
                        geode=state.geode + state.geode_robots,
                        clay_robots=state.clay_robots,
                        obsidian_robots=state.obsidian_robots,
                        ore_robots=state.ore_robots,
                    ),
                ),
            )
            if condition
        )

    return max(state.geode for state in queue)


blueprints = [Blueprint(*(map(int, re.findall(r"\d+", line)))) for line in open("./src/day19/input.txt").read().splitlines()]
print(sum(most_geodes(b, 24) * b.id for b in blueprints))
print(prod(most_geodes(b, 32) for b in blueprints[:3]))


## converted to real tuples brings runtime down from 10 to 1s
# from math import prod
# import re
# def most_geodes(blueprint: tuple[int, int, int, int, int, int, int], until: int):
#     queue = [(0, 0, 0, 0, 0, 0, 0, 1)]
#     for _ in range(0, until):
#         previous = sorted(queue)[-4000:]
#         queue = set(
#             new_state
#             for s in previous
#             for new_state in (
#                 (s[0] + s[1], s[1], s[2] + s[3], s[3], s[4] + s[5], s[5], s[6] + s[7], s[7]),
#                 blueprint[1] <= s[6] and (s[0] + s[1], s[1], s[2] + s[3], s[3], s[4] + s[5], s[5], s[6] + s[7] - blueprint[1], s[7] + 1),
#                 blueprint[2] <= s[6] and (s[0] + s[1], s[1], s[2] + s[3], s[3], s[4] + s[5], s[5] + 1, s[6] + s[7] - blueprint[2], s[7]),
#                 blueprint[3] <= s[6] and blueprint[4] <= s[4] and (s[0] + s[1], s[1], s[2] + s[3], s[3] + 1, s[4] + s[5] - blueprint[4], s[5], s[6] + s[7] - blueprint[3], s[7]),
#                 blueprint[5] <= s[6] and blueprint[6] <= s[2] and (s[0] + s[1], s[1] + 1, s[2] + s[3] - blueprint[6], s[3], s[4] + s[5], s[5], s[6] + s[7] - blueprint[5], s[7]),
#             )
#             if new_state
#         )
#     return max(state[0] for state in queue)
# blueprints = [tuple(map(int, re.findall(r"\d+", line))) for line in open("./src/day19/input.txt").read().splitlines()]
# print(sum(most_geodes(b, 24) * b[0] for b in blueprints), prod(most_geodes(b, 32) for b in blueprints[:3]))
