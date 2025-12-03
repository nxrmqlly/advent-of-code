from load_input import load_input


def max_joltage(battery_bank: str) -> tuple[int, str]:
    index, max_j = 0, "0"
    for k, joltage in enumerate(battery_bank):
        if joltage > max_j:
            max_j = joltage
            index = k
    return index, max_j


def joltage_str(bank: str, batt_count: int = 2):
    if batt_count == 2:
        idx, d1 = max_joltage(bank[:-1])
        _, d2 = max_joltage(bank[idx + 1 :])

        return d1 + d2

    idx, digit = max_joltage(bank[: -batt_count + 1])
    return digit + joltage_str(bank[idx + 1 :], batt_count - 1)


def part_one(batt_count: int = 2):
    banks = load_input()
    total = 0

    for bank in banks:
        total += int(joltage_str(bank, batt_count))

    print(f"total joltage: {total}")


if __name__ == "__main__":
    part_one(2)
    part_one(12)
