def display(knots: list["Knot"]):
    x_min = min(x for knot in knots for x, _ in knot.visited)
    x_max = max(x for knot in knots for (x, _) in knot.visited)
    y_min = min(y for knot in knots for (_, y) in knot.visited)
    y_max = max(y for knot in knots for (_, y) in knot.visited)

    for y in range(y_max + 2, y_min - 2, -1):
        for x in range(x_min - 2, x_max + 2):
            if (x, y) == (knots[0].x, knots[0].y):
                print("H", end="")
            elif (x, y) == (knots[1].x, knots[1].y):
                print("1", end="")
            elif (x, y) == (knots[2].x, knots[2].y):
                print("2", end="")
            elif (x, y) == (knots[3].x, knots[3].y):
                print("3", end="")
            elif (x, y) == (knots[4].x, knots[4].y):
                print("4", end="")
            elif (x, y) == (knots[5].x, knots[5].y):
                print("5", end="")
            elif (x, y) == (knots[6].x, knots[6].y):
                print("6", end="")
            elif (x, y) == (knots[7].x, knots[7].y):
                print("7", end="")
            elif (x, y) == (knots[8].x, knots[8].y):
                print("8", end="")
            elif (x, y) == (knots[9].x, knots[9].y):
                print("9", end="")
            elif (x, y) == (0, 0):
                print("s", end="")
            else:
                print(".", end="")
        print()
