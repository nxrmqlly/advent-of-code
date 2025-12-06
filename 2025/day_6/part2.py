from load_input import load_input


def regroup_and_int(list_to_group: list[tuple[str, ...]]) -> list[tuple[int]]:
    """
    <this definition is exremely jargonny>
    Regroups and cleans a list of tuples of strings into a list of tuples of integers,
    separating groups by tuples consisting of only spaces.
    """
    groups = []
    current_grp = []

    for item in list_to_group:
        combined = "".join(item).strip()
        if combined:
            current_grp.append(int(combined))
        else:  # combined = ""
            groups.append(tuple(current_grp))
            current_grp = []

    groups.append(tuple(current_grp))  # append the last group
    return groups


def simplify_to_dict(
    operators: list[str], gropued_values: list[list[int]]
) -> dict[tuple[int, ...], str]:
    """Maps tuples of integers to respective operator strings"""

    # make sure there is no mismatch
    assert len(operators) == len(gropued_values)

    # fin = dict()
    # for op_idx, op in enumerate(operators):
    #     # the numbers are mapped to --> operator
    #     fin[tuple(gropued_values[op_idx])] = op

    return {group: op for group, op in zip(gropued_values, operators)}


def calc_nums(nums: tuple[int], op: str) -> int:
    """Calculates sum or product of numbers"""
    assert op in ["+", "*"]

    if op == "+":
        return sum(nums)

    product = 1
    for k in nums:
        product *= k
    return product


def part_two():
    input_list = load_input()
    # width = len(input_list[0])

    # for item in input_list:
    #     assert len(item) == width

    *rows, op_row = input_list  # avoids mutating with .pop()

    # reverse, remove spaces and, turn into list
    # crazy one liner go brrrr
    operators = list(op_row[::-1].replace(" ", ""))

    transposed = [f for f in zip(*rows, strict=True)]
    grouped = regroup_and_int(transposed[::-1])
    simplified = simplify_to_dict(operators, grouped)  # not really needed but for fun

    total = 0

    for item in simplified.items():
        total += calc_nums(*item)  # nums, op

    print("\n".join(f"{op} -> {nums}" for nums, op in simplified.items()))
    print(f"total sum = {total}")


if __name__ == "__main__":
    part_two()
