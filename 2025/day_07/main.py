from load_input import load_input


def part_one():
    grid = load_input()
    ROWS = len(grid)
    COLS = len(grid[0])

    init_col = grid[0].index("S")

    # track the splits (set because it shouldn't duplicate as we iter over cols (cells))
    splits = set()

    # cols where active beams exist, init with start col
    curr_active = {init_col}

    for row in range(1, ROWS):
        new_active = set()  # for the NEXT row (empty)

        for col in curr_active:
            if grid[row][col] == ".":  # empty space, go directly below
                new_active.add(col)

            elif grid[row][col] == "^":  # hits splitter
                # track splitter coordinate (so it was split "here")
                # this is the correct approach as opposed to counting "^" because some "^" may never be hit
                splits.add((row, col))

                # * note how we DONT add the old beam pos here, only right and left
                # * this is because the beam only goes left and right, not downwards anymore
                # check bounds
                if col + 1 < COLS:
                    new_active.add(col + 1)
                if col - 1 >= 0:
                    new_active.add(col - 1)

            else:  # ! input mess up, lol :P
                print(
                    "YOU ARE A FUCKING DONKEY !!! >>> [ CHECK INPUT ] <<< !!! YOU IDIOT SANDWICH\n"
                    * 10
                )
                print("https://tenor.com/bvBar.gif")
                raise ValueError(f"Unexpected char '{grid[row][col]}' at {row},{col}")

        curr_active = new_active  # move down a row

    return len(splits)


def part_two():
    grid = load_input()
    ROWS = len(grid)
    COLS = len(grid[0])

    init_col = grid[0].index("S")

    curr_vals = [0] * COLS
    curr_vals[init_col] = 1  # start with a single beam with 1 intensity

    for row in range(1, ROWS):
        new_vals = [0] * COLS  # the list for tracking the NEXT row's intensities

        for col in range(0, COLS):
            old_val = curr_vals[col]  # what the old val was

            if old_val == 0:  # no beam here, skip
                continue

            if grid[row][col] == ".":  # if the cell is empty, straight down
                new_vals[col] += old_val  # update intensity for next row

            # cell is splitter, "pascal triangle" here, splits left and right
            elif grid[row][col] == "^":
                # even if the val for the col is set,
                # we will add the "old" or current value to that cell to increase intensity

                # * even if new_vals[col] already has a value,
                # * we use += old_val instead of replacing the whole new_vals[col +- 1].
                # * whyyyy? because... multiple beams may converge on the same column.
                # * when that happens, their intensities should sum up:
                # * and also, we are looping through the cols (cells) right now, so we might need to add intensity:
                # *     combined intensity = sum(parent intensities)
                # *
                # * essentially how "pascal's triangle" (here) works:
                # * new[col] = old[col-1] + old[col+1]

                # check bounds
                if col + 1 < COLS:  # right: combine intensities
                    new_vals[col + 1] += old_val

                if col - 1 >= 0:  # left: add old intensity to this side
                    new_vals[col - 1] += old_val

            else:  # ! input mess up, lol :P
                print(
                    "YOU ARE A FUCKING DONKEY !!! >>> [ CHECK INPUT ] <<< !!! YOU IDIOT SANDWICH\n"
                    * 10
                )
                print("https://tenor.com/bvBar.gif")
                raise ValueError(f"Unexpected char '{grid[row][col]}' at {row},{col}")

        curr_vals = new_vals  # move down one row

    return sum(curr_vals)  # sum of all timelines results at the end


if __name__ == "__main__":
    res1 = part_one()
    res2 = part_two()

    print(f"total splits:    {res1}")
    print(f"total timelines: {res2}")
