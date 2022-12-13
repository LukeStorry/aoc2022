from functools import cmp_to_key


def compare(left, right):
    match left, right:
        case [_, *_], []:
            return False
        case [], [_, *_]:
            return True
        case [l, *l_tail], [r, *r_tail]:
            match l, r:
                case int(l), int(r):
                    return l < r if l != r else compare(l_tail, r_tail)
                case [*l], [*r]:
                    return (
                        compare(l, r)
                        if compare(l, r) != "backtrack"
                        else compare(l_tail, r_tail)
                    )
                case int(l), [*r]:
                    return (
                        compare([l], r)
                        if compare([l], r) != "backtrack"
                        else compare(l_tail, r_tail)
                    )
                case [*l], int(r):
                    return (
                        compare(l, [r])
                        if compare(l, [r]) != "backtrack"
                        else compare(l_tail, r_tail)
                    )
        case [], []:
            return "backtrack"


data = open("./src/day13/input.txt").read()
pairs = [list(map(eval, l.splitlines())) for l in data.split("\n\n")]
print(sum(i for i, pair in enumerate(pairs, 1) if compare(*pair)))

new_1, new_2 = [[2]], [[6]]

packets = sorted(
    [new_1] + [new_2] + [p for pair in pairs for p in pair],
    key=cmp_to_key(lambda x, y: -1 if compare(x, y) else 1),
)

print((packets.index(new_1) + 1) * (packets.index(new_2) + 1))
