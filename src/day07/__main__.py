from dataclasses import dataclass

data = open("./src/day07/input.txt").read()


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: "Directory"
    files: list[File]
    dirs: list["Directory"]
    size: int = 0


current = Directory("/", None, [], [])
all = [current]
for command in data.splitlines():
    match command.split():
        case [_, "cd", ".."]:
            current = current.parent
        case [_, "cd", "/"]:
            current = all[0]
        case [_, "cd", name]:
            current = next(d for d in current.dirs if d.name == name)
        case [_, "ls"]:
            pass
        case ["dir", name]:
            new = Directory(name, current, [], [])
            all.append(new)
            current.dirs.append(new)
        case [size, name] if size.isnumeric():
            current.files.append(File(name, int(size)))
        case x:
            print("ERROR COULDNT PARSE: " + str(x))

# dynamic programming: can start from the bottom and work up
for dir in reversed(all):
    dir.size = sum(x.size for x in dir.files + dir.dirs)


print(sum(x.size for x in all if x.size < 100000))
print(
    next(
        d.size
        for d in sorted(all, key=lambda x: x.size)
        if d.size >= (all[0].size - 40000000)
    )
)
