from models import Machine

test_dat = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


def load_input(test: bool = False) -> dict:
    if test:
        dat = test_dat.strip()
    else:
        with open("2025/input/day_10.txt") as f:
            dat = f.read().strip()
    machines = []

    for line in dat.splitlines():
        things = line.split(" ")
        machines.append(
            Machine(
                solution=[led == "#" for led in things[0][1:-1]],
                buttons=[tuple(map(int, x[1:-1].split(","))) for x in things[1:-1]],
                joltages=[int(x) for x in things[-1][1:-1].strip().split(",")],
            )
        )
    return machines
