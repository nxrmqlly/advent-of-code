from load_input import load_input


def parse(rows: list[str]) -> list[list[str]]:
    new_rows = []
    for row in rows:
        new_rows.append(row.split())

    return new_rows


def calc_nums(nums: list[int], op: str) -> int:
    """Calculates sum or product of numbers"""
    assert op in ["+", "*"]

    if op == "+":
        return sum(nums)

    product = 1
    for k in nums:
        product *= k
    return product


def part_one():
    rows = parse(load_input())
    all_ans = []

    # rwcs = len(rows)
    # cols = len(rows[0])
    # transposed = [[0 for _ in range(rwcs)] for _ in range(cols)]
    # for i in range(rwcs):
    #     for j in range(cols):
    #         transposed[j][i] = rows[i][j]

    transposed = [list(x) for x in zip(*rows, strict=True)]

    for row in transposed:
        *nums, op = row  # as opposed to row.pop() which mutates the list

        all_ans.append(calc_nums([int(num) for num in nums], op))

    print(f"{all_ans=}\nsum = {sum(all_ans)}")


if __name__ == "__main__":
    part_one()
