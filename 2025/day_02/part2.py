from load_input import load_inp

# needed some help with this but fine
def part_two():
    ranges = load_inp()
    total = 0

    for rng in ranges:
        L, R = [int(f) for f in rng.split("-")]

        for i in range(L, R + 1):

            txt = str(i)
            length = len(txt)

            for n in range(1, length + 1):
                # skip if not a factor
                if not length % n == 0: 
                    continue

                # trivial: skip of eql length
                if n == length:
                    continue

                pattern = txt[:n]

                # check if txt is made of repeated blocks
                checking = pattern * (length // n)

                if checking == txt:
                    print(f"repeating: {txt}")
                    total += i
                    break

    print(f"total is: {total}")


# this solution is bad and i overithinked it.
# this only works for even length numbers
# ! OONT USE ; not even worth looking >:)
def part_two_OLD_DONT_USE():
    ranges = load_inp()
    # total = 0

    for rng in ranges:
        L, R = [int(f) for f in rng.split("-")]

        # if not even lengthed, it wont work
        for i in range(L, R + 1):
            txt = str(i)
            length = len(txt)

            len_factors = []
            for j in range(1, length + 1):
                if length % j == 0 and not length == j:
                    len_factors.append(j)

            is_duped = False

            for len_factor in len_factors:

                first_spl = txt[:len_factor]

                possible_dupes = length // len_factor

                for ix, dupe_p in enumerate(range(possible_dupes)):

                    if txt[dupe_p * (ix + 1) : 2 * dupe_p * (ix + 1)] == first_spl:
                        is_duped = True
                    else:
                        is_duped = False

            if is_duped:
                print(txt)


if __name__ == "__main__":
    part_two()
