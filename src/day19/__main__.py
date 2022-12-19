from math import prod
import re
from typing import NamedTuple

class State(NamedTuple):
    geode: int = 0
    geode_robots: int = 0
    obsidian: int = 0
    obsidian_robots: int = 0
    ore_robots: int = 0
    clay_robots: int = 0
    clay: int = 0
    ore: int = 0

class Blueprint(NamedTuple):
    id: int
    ore_ore: int
    clay_ore: int
    obsidian_ore: int
    obsidian_clay: int
    geode_ore: int
    geode_obsidian: int

def most_geodes(blueprint: Blueprint, until: int):
    queue = [State(ore_robots=1)]
    for _ in range(0, until):
        previous = sorted(queue)[-10000:]
        queue = set()
        for state in previous:
            queue.add(
                State(
                    ore=state.ore + state.ore_robots,
                    clay=state.clay + state.clay_robots,
                    obsidian=state.obsidian + state.obsidian_robots,
                    geode=state.geode + state.geode_robots,
                    ore_robots=state.ore_robots,
                    clay_robots=state.clay_robots,
                    obsidian_robots=state.obsidian_robots,
                    geode_robots=state.geode_robots,
                )
            )
            if blueprint.ore_ore <= state.ore:
                queue.add(
                    State(
                        ore_robots=state.ore_robots + 1,
                        ore=state.ore + state.ore_robots - blueprint.ore_ore,
                        clay=state.clay + state.clay_robots,
                        obsidian=state.obsidian + state.obsidian_robots,
                        geode=state.geode + state.geode_robots,
                        clay_robots=state.clay_robots,
                        obsidian_robots=state.obsidian_robots,
                        geode_robots=state.geode_robots,
                    )
                )
            if blueprint.clay_ore <= state.ore:
                queue.add(
                    State(
                        clay_robots=state.clay_robots + 1,
                        ore=state.ore + state.ore_robots - blueprint.clay_ore,
                        clay=state.clay + state.clay_robots,
                        obsidian=state.obsidian + state.obsidian_robots,
                        geode=state.geode + state.geode_robots,
                        ore_robots=state.ore_robots,
                        obsidian_robots=state.obsidian_robots,
                        geode_robots=state.geode_robots,
                    )
                )
            if blueprint.obsidian_ore <= state.ore and blueprint.obsidian_clay <= state.clay:
                queue.add(
                    State(
                        obsidian_robots=state.obsidian_robots + 1,
                        ore=state.ore + state.ore_robots - blueprint.obsidian_ore,
                        clay=state.clay + state.clay_robots - blueprint.obsidian_clay,
                        obsidian=state.obsidian + state.obsidian_robots,
                        geode=state.geode + state.geode_robots,
                        ore_robots=state.ore_robots,
                        clay_robots=state.clay_robots,
                        geode_robots=state.geode_robots,
                    )
                )
            if blueprint.geode_ore <= state.ore and blueprint.geode_obsidian <= state.obsidian:
                queue.add(
                    State(
                        geode_robots=state.geode_robots + 1,
                        ore=state.ore + state.ore_robots - blueprint.geode_ore,
                        obsidian=state.obsidian + state.obsidian_robots - blueprint.geode_obsidian,
                        clay=state.clay + state.clay_robots,
                        geode=state.geode + state.geode_robots,
                        clay_robots=state.clay_robots,
                        obsidian_robots=state.obsidian_robots,
                        ore_robots=state.ore_robots,
                    )
                )
    return max(state.geode for state in queue)


blueprints = [Blueprint(*(map(int, re.findall(r"\d+", line)))) for line in open("./src/day19/input.txt").read().splitlines()]
print(sum(most_geodes(b, 24) * b.id for b in blueprints))
print(prod(most_geodes(b, 32) for b in blueprints[:3]))