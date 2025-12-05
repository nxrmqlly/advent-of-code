test_dat = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def load_input(test: bool = False) -> tuple[list[tuple[int, int]], list[int]]:
    if test:
        dat = test_dat.strip()
    else:
        dat = open("./2025/input/day_5.txt").read().strip()

    ranges, ingredients = dat.split("\n\n")

    # parse ingredients
    ingredients = [int(x) for x in ingredients.split("\n")]

    # parse ranges
    fin_ranges = []
    for line in ranges.split("\n"):
        low, high = map(int, line.split("-"))
        fin_ranges.append((int(low), int(high)))

    return fin_ranges, ingredients
