def load_inp() -> list[str]:
    with open("./2025/input/day_2.txt") as f:
        ranges = f.read().strip().split(",")

    return ranges
