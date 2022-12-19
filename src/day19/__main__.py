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

    def no_build(s: "State", bp: "Blueprint"):
        return State(
            ore=s.ore + s.ore_robots,
            clay=s.clay + s.clay_robots,
            obsidian=s.obsidian + s.obsidian_robots,
            geode=s.geode + s.geode_robots,
            ore_robots=s.ore_robots,
            clay_robots=s.clay_robots,
            obsidian_robots=s.obsidian_robots,
            geode_robots=s.geode_robots,
        )

    def build_ore_robot(s: "State", bp: "Blueprint"):
        return State(
            ore_robots=s.ore_robots + 1,
            ore=s.ore + s.ore_robots - bp.ore_robot_ore_cost,
            clay=s.clay + s.clay_robots,
            obsidian=s.obsidian + s.obsidian_robots,
            geode=s.geode + s.geode_robots,
            clay_robots=s.clay_robots,
            obsidian_robots=s.obsidian_robots,
            geode_robots=s.geode_robots,
        )

    def build_clay_robot(s: "State", bp: "Blueprint"):
        return State(
            clay_robots=s.clay_robots + 1,
            ore=s.ore + s.ore_robots - bp.clay_robot_ore_cost,
            clay=s.clay + s.clay_robots,
            obsidian=s.obsidian + s.obsidian_robots,
            geode=s.geode + s.geode_robots,
            ore_robots=s.ore_robots,
            obsidian_robots=s.obsidian_robots,
            geode_robots=s.geode_robots,
        )

    def build_obsidian_robot(s: "State", bp: "Blueprint"):
        return State(
            obsidian_robots=s.obsidian_robots + 1,
            ore=s.ore + s.ore_robots - bp.obsidian_robot_ore_cost,
            clay=s.clay + s.clay_robots - bp.obsidian_robot_clay_cost,
            obsidian=s.obsidian + s.obsidian_robots,
            geode=s.geode + s.geode_robots,
            ore_robots=s.ore_robots,
            clay_robots=s.clay_robots,
            geode_robots=s.geode_robots,
        )

    def build_geode_robot(s: "State", bp: "Blueprint"):
        return State(
            geode_robots=s.geode_robots + 1,
            ore=s.ore + s.ore_robots - bp.geode_robot_ore_cost,
            obsidian=s.obsidian + s.obsidian_robots - bp.geode_robot_obsidian_cost,
            clay=s.clay + s.clay_robots,
            geode=s.geode + s.geode_robots,
            clay_robots=s.clay_robots,
            obsidian_robots=s.obsidian_robots,
            ore_robots=s.ore_robots,
        )


class Blueprint(NamedTuple):
    id: int
    ore_robot_ore_cost: int
    clay_robot_ore_cost: int
    obsidian_robot_ore_cost: int
    obsidian_robot_clay_cost: int
    geode_robot_ore_cost: int
    geode_robot_obsidian_cost: int

    def most_geodes(self, until=24):
        queue = set([State(ore_robots=1)])
        for _ in range(0, until):
            new_queue = set()
            for state in sorted(queue)[-10000:]:
                if (
                    state.ore >= self.geode_robot_ore_cost
                    and state.obsidian >= self.geode_robot_obsidian_cost
                ):
                    new_queue.add(state.build_geode_robot(self))
                    # continue

                if (
                    state.ore >= self.obsidian_robot_ore_cost
                    and state.clay >= self.obsidian_robot_clay_cost
                ):
                    new_queue.add(state.build_obsidian_robot(self))

                new_queue.add(state.no_build(self))
                if state.ore >= self.ore_robot_ore_cost:
                    new_queue.add(state.build_ore_robot(self))
                if state.ore >= self.clay_robot_ore_cost:
                    new_queue.add(state.build_clay_robot(self))

            queue = new_queue
        return max(state.geode for state in queue)


data = open("./src/day19/input.txt").read()
blueprints = [Blueprint(*(map(int, re.findall(r"\d+", line)))) for line in data.splitlines()]
print(sum(b.most_geodes() * b.id for b in blueprints))
