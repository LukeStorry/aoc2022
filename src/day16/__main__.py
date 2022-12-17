import re
from dataclasses import dataclass


@dataclass
class Valve:
    name: str
    flow_rate: int
    leads_to: list[str]

    def __hash__(self):
        return hash(self.name)


valves = [
    Valve(name, int(rate), leads_to.split(", "))
    for name, rate, leads_to in re.findall(
        r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)",
        open("./src/day16/input.txt").read(),
    )
]

distances = {
    (v, to): 1 if to.name in v.leads_to else 999999
    for to in valves
    for v in valves
}

for c in valves:
    for a in valves:
        for b in valves:
            distances[a, b] = min(
                distances[a, b],
                distances[a, c] + distances[c, b],
            )


def try_paths(
    current: Valve,
    minute: int,
    opened=frozenset(),
    pressure=0,
    found_pressures: dict[frozenset[str], int] = {},
):
    found_pressures[opened] = max(pressure, found_pressures.get(opened, 0))
    for next in valves:
        if next.flow_rate == 0:
            continue
        mins_left = minute - 1 - distances[current, next]
        if next.name in opened or mins_left <= 0:
            continue

        try_paths(
            next,
            mins_left,
            frozenset(opened.union([next.name])),
            pressure + next.flow_rate * mins_left,
        )
    return found_pressures


AA = next(v for v in valves if v.name == "AA")
print(max(try_paths(AA, 30).values()))

part_2_run = try_paths(AA, 26)
print(
    max(
        my_pressure + elephant_pressure
        for my_path, my_pressure in part_2_run.items()
        for elephant_path, elephant_pressure in part_2_run.items()
        if my_path.isdisjoint(elephant_path)
    )
)
