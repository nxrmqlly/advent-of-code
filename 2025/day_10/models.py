from typing import NamedTuple


class Machine(NamedTuple):
    solution: list[bool]
    buttons: list[tuple[int, ...]]
    joltages: list[int]
