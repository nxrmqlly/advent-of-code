"""
The exact same logic except there are no quirky python one liners
"""

from load_input import load_input
from merge_ranges import merge_ranges


def part_one():
    ranges, ingredients = load_input()
    merged = merge_ranges(ranges)

    fresh_count = 0

    for ingredient in ingredients:
        for low, high in merged:
            if low <= ingredient <= high:
                fresh_count += 1
                break

    return fresh_count


def part_two():
    ranges, _ = load_input()
    merged = merge_ranges(ranges)

    max_fresh = 0

    for low, high in merged:
        max_fresh += high - low + 1  # +1 to include both low and high

    return max_fresh


if __name__ == "__main__":
    res1 = part_one()
    res2 = part_two()

    print(f"result one: {res1}\nresult two: {res2}")
