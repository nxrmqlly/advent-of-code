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

    with open("./2025/input/day_4.txt") as f:
        rows = f.read().strip().split("\n")
        
    return rows
