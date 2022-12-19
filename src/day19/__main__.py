from dataclasses import dataclass, field, replace
import re


@dataclass(frozen=True, slots=True)
class State:
    minute: int = 1
    ore_robots: int = 1
    ore: int = 1
    clay_robots: int = 0
    clay: int = 0
    obsidian_robots: int = 0
    obsidian: int = 0
    geode_robots: int = 0
    geodes: int = 0

    def is_invalid(self, bp: "Blueprint", until: int):
        max_ore_needed = max(
            bp.clay_robot_ore_cost,
            bp.obsidian_robot_ore_cost,
            bp.geode_robot_ore_cost,
        )
        return (
            any(s < 0 for s in (self.ore, self.clay, self.obsidian))
            or self.ore > max_ore_needed - self.ore_robots * 2 + 3
            # or self.ore_robots > max_ore_needed *2
            or self.clay > bp.obsidian_robot_clay_cost * 2 - self.clay_robots + 3
            # or self.clay_robots > bp.obsidian_robot_clay_cost
            or self.obsidian > bp.geode_robot_obsidian_cost - self.obsidian_robots + 3
            or self.minute > until + 1
            # or (self.minute < 5 and not self.geode_robots)
        )

    def __lt__(self, other):
        if self.minute < other.minute:
            return False
        return (
            self.ore_robots < other.ore_robots
            and self.clay_robots < other.clay_robots
            and self.obsidian_robots < other.obsidian_robots
            and self.geode_robots < other.geode_robots
        )

    def next(self):
        return replace(
            self,
            minute=self.minute + 1,
            ore=self.ore + self.ore_robots,
            clay=self.clay + self.clay_robots,
            obsidian=self.obsidian + self.obsidian_robots,
            geodes=self.geodes + self.geode_robots,
        )

    def add_ore_robot(self, bp: "Blueprint"):
        next = self.next().next()
        return replace(
            next,
            ore_robots=next.ore_robots + 1,
            ore=next.ore - bp.ore_robot_ore_cost,
        )

    def add_clay_robot(self, bp: "Blueprint"):
        next = self.next().next()
        return replace(
            next,
            clay_robots=self.clay_robots + 1,
            ore=next.ore - bp.clay_robot_ore_cost,
        )

    def add_obsidian_robot(self, bp: "Blueprint"):
        next = self.next().next()
        return replace(
            next,
            obsidian_robots=next.obsidian_robots + 1,
            ore=next.ore - bp.obsidian_robot_ore_cost,
            clay=next.clay - bp.obsidian_robot_clay_cost,
        )

    def add_geode_robot(self, bp: "Blueprint"):
        next = self.next().next()
        return replace(
            next,
            geode_robots=next.geode_robots + 1,
            ore=next.ore - bp.geode_robot_ore_cost,
            obsidian=next.obsidian - bp.geode_robot_obsidian_cost,
        )

    def __str__(self) -> str:
        return f"[m:{self.minute:<2} or:{self.ore_robots:<2} o:{self.ore:<2} cr:{self.clay_robots:<2} c:{self.clay:<2} obr:{self.obsidian_robots:<2} ob:{self.obsidian:<2} gr:{self.geode_robots:<2} g:{self.geodes:<2}]"

    def __repr__(self) -> str:
        return str(self)


@dataclass(frozen=True, slots=True)
class Blueprint:
    id: int
    ore_robot_ore_cost: int
    clay_robot_ore_cost: int
    obsidian_robot_ore_cost: int
    obsidian_robot_clay_cost: int
    geode_robot_ore_cost: int
    geode_robot_obsidian_cost: int


def find_most_geodes(self, until=24):
    queue = [tuple((State(),))]
    found = []
    while queue:
        trail = queue.pop(0)
        current_state = trail[-1]
        if current_state.is_invalid(self, until):
            continue
        # if any(state < s for s in self.states):
        # return 0
        if current_state.minute >= until:
            found.append((trail, current_state.geodes))
        # if state.minute == 2:
        # return state.geodes + state.geode_robots
        # if state in self.states:
        #     return self.states[state]

        # print(current_state)
        for next in (
            current_state.add_geode_robot(self),
            current_state.add_obsidian_robot(self),
            current_state.add_clay_robot(self),
            current_state.add_ore_robot(self),
            current_state.next(),
        ):
            if next.is_invalid(self, until):
                continue
            if any(next < t[-1] for t in queue):
                continue

            queue.append(trail + (next,))

    print(max(found, key=lambda f: f[1]))
    return max(f[1] for f in found)


data = open("./src/day19/example.txt").read()
example = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""

blueprints = [Blueprint(*(map(int, re.findall(r"\d+", line)))) for line in data.splitlines()]

print(find_most_geodes(blueprints[0]))
print(find_most_geodes(blueprints[1]))
# print(sum(find_most_geodes(b) * b.id for b in blueprints))
