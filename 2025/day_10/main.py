from load_input import load_input
from itertools import combinations
from models import Machine
import z3  # im sorry


def part_one():
    machines: list[Machine] = load_input()
    total_presses = 0

    for machine in machines:
        presses_this_machine = 0
        lights = [False] * len(machine.solution)

        while lights != machine.solution:
            presses_this_machine += 1
            # this gives nCk, nCk+1 ... combinations of button presses
            # k depends on how many presses we've done so far,
            # so we try all combinations of button presses of size presses_this_machine
            for cb in combinations(range(len(machine.buttons)), presses_this_machine):

                # init new lights for comparison
                new_lights = [False] * len(machine.solution)

                for btn in cb:
                    for b in machine.buttons[btn]:
                        new_lights[b] = not new_lights[b]  # toggle light state

                if new_lights == machine.solution:
                    lights = new_lights
                    break

        total_presses += presses_this_machine
    return total_presses


def part_two():
    total_presses = 0
    machines: list[Machine] = load_input()

    for machine in machines:
        solver = z3.Solver()

        bvars = [
            z3.Int(f"b{i}") for i in range(len(machine.buttons))
        ]  # button variables

        for b in bvars:
            solver.add(b >= 0)  # each button pressed 0 or 1 times

        for idx, jolt in enumerate( machine.joltages):
            vvrs = [bvars[j] for j, button in enumerate(machine.buttons) if idx in button]
            solver.add(
                z3.Sum(vvrs) == jolt
            )

        while solver.check() == z3.sat:
            model = solver.model()
            n = sum(model[d].as_long() for d in bvars)
            solver.add(z3.Sum(bvars) < n )

        total_presses += n
    return total_presses

if __name__ == "__main__":
    res1 = part_one()
    print(f"Part One: {res1}")
    res2 = part_two()
    print(f"Part Two: {res2}")
