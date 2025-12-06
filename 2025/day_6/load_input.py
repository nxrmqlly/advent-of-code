test_dat = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def load_input(test: bool = False) -> list[str]:
    if test:
        dat = test_dat.strip("\n")
    else:
        with open("./2025/input/day_6.txt") as f:
            dat = f.read().strip("\n")

    return dat.split("\n")
