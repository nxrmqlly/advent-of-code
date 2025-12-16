import math

from load_input import load_input

def find_dist(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> int:
    return math.dist(p1, p2)

def init_dists_circuits(junctions_points):
    dists = []  # [ (distance, (point1, point2)) ... ]
    circuits = []

    for i, jnc1 in enumerate(junctions_points):
        for j, jnc2 in enumerate(junctions_points):
            if i < j:  # avoids double counting and self-comparison
                dists.append((find_dist(jnc1, jnc2), (jnc1, jnc2)))

    dists.sort(key=lambda x: x[0])
    circuits = [{c_jnc} for c_jnc in junctions_points]

    return dists, circuits

def first_item(it):
    return next(iter(it))


def part_one() -> None:
    ATTEMPTS = 1000
    junctions_points = load_input()

    dists, circuits = init_dists_circuits(junctions_points)

    max_circuit_length = len(junctions_points)
    print(f"Max circuit length: {max_circuit_length}")
    processed = 0
    connections_temp = []

    for _dist, (jnc1, jnc2) in dists:
        jnc1_circuit = first_item(x for x in circuits if jnc1 in x)
        jnc2_circuit = first_item(x for x in circuits if jnc2 in x)
        
        if jnc1_circuit != jnc2_circuit:
            jnc1_circuit.update(jnc2_circuit)
            jnc2_circuit.clear()

        processed += 1
        if processed == ATTEMPTS:
            break

        connections_temp.append((jnc1, jnc2))

    ### finally compute sizes

    sizes = sorted(len(c) for c in circuits if c)

    # If fewer than 3 circuits exist, pad with 1
    while len(sizes) < 3:
        sizes.insert(0, 1)

    print(sizes)

    a, b, c = sizes[-3:]
    print(a * b * c)


def part_two() -> None:

    junctions_points = load_input()

    dists, circuits = init_dists_circuits(junctions_points)
    
    max_circuit_length = len(junctions_points)
    last_merge = None

    # Kruskal-like merging
    for dist, (jnc1, jnc2) in dists:
        jnc1_circuit = first_item(c for c in circuits if jnc1 in c)
        jnc2_circuit = first_item(c for c in circuits if jnc2 in c)

        if jnc1_circuit != jnc2_circuit:
            jnc1_circuit.update(jnc2_circuit)
            jnc2_circuit.clear()
            last_merge = (jnc1, jnc2)

            if len(jnc1_circuit) == max_circuit_length:
                break

    jnc1, jnc2 = last_merge
    print(f"Last merge  : {jnc1} <-> {jnc2}")
    print(f"Product of X: {jnc1[0] * jnc2[0] = }")


if __name__ == "__main__":
    part_one()
    part_two()
