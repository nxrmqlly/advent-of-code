from load_input import load_input
from collections import deque
from functools import cache  # all hail cache


def part_one():
    devices = load_input()

    first_device = devices.pop("you")
    total_ways = 0

    next_state_check = deque([*first_device.connections])

    while next_state_check:
        checking = next_state_check.popleft()
        if checking == "out":
            total_ways += 1
            continue
        else:
            next_state_check.extend(devices.get(checking).connections)

    return total_ways


# ARRRRRRRRRRR THIS WAS SO HARD
def part_two():
    devices = load_input()

    @cache  # saving grace, else it takes millions of years
    def count_paths(device: str, visited_dac: bool, visited_fft: bool) -> int:
        if device == "out":
            if visited_dac and visited_fft:
                return 1  # final path to add
            else:
                return 0  # moooooooove on

        match device:
            case "dac":
                visited_dac = True

            case "fft":
                visited_fft = True

        total_count = 0

        for dconn in devices[device].connections:
            total_count += count_paths(dconn, visited_dac, visited_fft)

        return total_count

    return count_paths("svr", False, False)


if __name__ == "__main__":
    ret1 = part_one()
    print("Part One:", ret1)
    ret2 = part_two()
    print("Part Two:", ret2)
