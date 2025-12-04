from load_input import load_input


seek = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))


def check_nearby(rows, x, y):
    count_nearby = 0
    max_y = len(rows)
    max_x = len(rows[0])

    for dx, dy in seek:  # check all relative / (d)elta positions
        nx, ny = x + dx, y + dy  # nx, ny = new x, new y :D

        if 0 <= nx < max_x and 0 <= ny < max_y:  # check if in bounds
            
            count_nearby += rows[ny][nx] == "@" # * Python trick: Because, True = 1, lol
                 

    return count_nearby


def part_one():
    rows = load_input()
    total_movable = 0

    for y, row in enumerate(rows):
        for x, item in enumerate(row):
            if item != "@":
                continue

            nearby = check_nearby(rows, x, y)
            print(f"{nearby=}, ({x}, {y})")

            if nearby <= 3:
                total_movable += 1

    print(f"{total_movable=}")
    return total_movable


def part_two():
    rows = [list(r) for r in load_input()]
    total_movable = 0

    while True:

        ### ! This logic was beautiful, but not needed in the end :( 
        ### ! Seems like, without copy is faster, it has the same work anyways 
        ### ! without copy time: 8.152340s, 9.975292s, 8.786981s 
        ### ! with copy time: 10.806175s, 14.117379s, 12.503559s 
        
        # check_nearby() when checking the in-place replaced row, could return bad results.
        # this creates a shallow copy of old grid so I dont have such problems.
        # old_rows = [
        #     row[:]  # * as, row[:] == row.copy() == list(row) == copy.copy(row)
        #     for row in rows
        # ]
        
        movable_this_iter = 0

        for y, row in enumerate(rows): # or, old_rows for safety
            for x, item in enumerate(row):
                if not item == "@":
                    continue

                nearby = check_nearby(rows, x, y) # or, old_rows for safety
                print(f"{nearby=}, ({x}, {y})")

                if nearby <= 3:
                    total_movable += 1
                    movable_this_iter += 1

                    rows[y][x] = "."

        if movable_this_iter == 0:
            break

    print(f"{total_movable=}")
    return total_movable


if __name__ == "__main__":
    res1 = part_one()
    res2 = part_two()

    print(f"total movable 1 = {res1}\n" f"total movable 2 = {res2}")
