from load_input import load_input
from merge_ranges import merge_ranges

def part_one():
    ranges, ingredients = load_input()
    merged = merge_ranges(ranges)

    return sum(
        any(
            # loop over each range for each ingredient
            low <= ingredient <= high  # check existence in range
            for low, high in merged
        )
        for ingredient in ingredients  # loop over each ingredient
    )


def part_two():
    ranges, _ = load_input()
    merged = merge_ranges(ranges)

    return sum(
        high - low + 1 for low, high in merged  # +1 to include both low and high
    )


if __name__ == "__main__":
    res1 = part_one()
    res2 = part_two()

    print(f"result one: {res1}\nresult two: {res2}")
