test_dat = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def load_input(test: bool = False) -> list[str]:
    if test:
        return test_dat.strip().split("\n")
    r = open("./2025/input/day_4.txt").read().strip()
    return r.split("\n")
