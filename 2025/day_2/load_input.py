def load_inp() -> list[str]:
    r = open("./2025/input/day_2.txt").read().strip()
    ranges = r.split(",")

    return ranges
