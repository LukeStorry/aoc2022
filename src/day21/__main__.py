import re

input = open("./src/day21/input.txt").read()
exec(re.sub(r"\(\)(\w+)", r"\1()", input.replace(": ", "=lambda:").replace(" ", "()")))
print(int(root()))

