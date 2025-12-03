def load_inp():
    r = open("./2025/input/day_2.txt").read().strip()
    ranges = r.split(",")

    return ranges


def part_one():
    ranges = load_inp()
    total = 0

    for rng in ranges:
        L, R = [int(f) for f in rng.split("-")]

        # if not even lengthed, it wont work
        for i in range(L, R + 1):
            txt = str(i)
            if len(txt) % 2 == 1:
                continue

            idx_c = (len(txt) // 2)

            # print(txt, idx_c, txt[0:idx_c], txt[idx_c:])

            if txt[0:idx_c] == txt[idx_c:]:
                print(txt)
                total += i
    print(f"Total Sum: {total}")


if __name__ == "__main__":
    part_one()
