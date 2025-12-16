test_dat = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


def load_input(test: bool = False) -> list[tuple[int, int]]:
    if test:
        data = test_dat.strip().splitlines()
    else:
        with open("2025/input/day_9.txt", "r") as f:
            data = f.read().strip().splitlines()

    points = []
    for line in data:
        x_str, y_str = line.split(",")
        points.append((int(x_str), int(y_str)))

    return points
