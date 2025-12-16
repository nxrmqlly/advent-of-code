from load_input import load_input


def construct_grid():
    points = load_input(True)
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in points:
        grid[y][x] = "#"

    for row in grid:
        print("".join(row))


def check_rectangle(
    ylines: list[list[int, int]], p1: tuple[int], p2: tuple[int]
) -> bool:
    x1, y1 = p1
    x2, y2 = p2

    # ensure x1 <= x2 && y1 <= y2
    # swap for ease of coding
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    for y in range(y1, y2 + 1):
        compare_x1, compare_x2 = ylines[y]
        if (
            (x1 < compare_x1)
            or (x1 > compare_x2)
            or (x2 < compare_x1)
            or (x2 > compare_x2)
        ):
            return False

    return True


def calc_area(p1, p2):
    ix, iy = p1
    jx, jy = p2
    return (abs(ix - jx) + 1) * (abs(iy - jy) + 1)


def print_lines(*, ylines: list, max_x: int):
    for y, line in enumerate(ylines):
        if line is None:
            print("." * (max_x + 2))
        else:
            sx1, sx2 = line
            print(f"{'.' * sx1}{'X' * (sx2 - sx1 + 1)}{'.' * (max_x + 1 - sx2)}")
    print()


def part_one() -> int:
    points = load_input()

    last_ar = 0
    largest_area_points = None

    for ix, iy in points:
        for jx, jy in points:
            area = calc_area((ix, iy), (jx, jy))
            if area > last_ar:
                last_ar = area
                largest_area_points = ((ix, iy), (jx, jy))
            print(f"Area between ({ix},{iy}) and ({jx},{jy}): {area}")

    print(f"Largest area is {last_ar} between points {largest_area_points}")

    return last_ar


def part_two() -> int:
    points = load_input()
    # max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])

    ylines = [None for _ in range(max_y + 2)]
    points.append(points[0])  # closes loop

    for i in range(1, len(points)):

        x1, y1 = points[i - 1]
        x2, y2 = points[i]

        # ensure x1 <= x2 && y1 <= y2
        # swap for ease of coding
        if x1 > x2:
            x1, x2 = x2, x1  # swap

        if y1 > y2:
            y1, y2 = y2, y1  # swap

        for y in range(y1, y2 + 1):  # loop over all y ranges in the 2 selected points
            if ylines[y] is None:  # line is empty
                ylines[y] = [x1, x2]  # set the line to points in comparison

            else:  # line is not empty
                dx1, dx2 = ylines[y]  # grab existing line to compare
                ylines[y] = [min(dx1, x1), max(dx2, x2)]  # find bigger bounding box

        # print_lines(ylines=ylines, max_x=max_x) # ? show progress grid
        print(f"constructed: {points[i-1]} to {points[i]}")
    # print_lines(ylines=ylines, max_x=max_x) # ? show final grid
    print("--- Done constructing lines ---")

    last_area = 0


    print("--- Calculating max area... ---\nswaps:")
    # brute force all combinations of points to find largest area
    for point_i in points:
        x1, y1 = point_i

        for point_j in points[1:]:
            x2, y2 = point_j

            if x1 != x2 and y1 != y2:
                new_area = calc_area(point_i, point_j)
                if new_area > last_area and check_rectangle(ylines, point_i, point_j):
                    last_area = new_area
                    print(f"swap: {last_area}")
                    
    print("--> final: ",last_area) # final
    return last_area


if __name__ == "__main__":
    res1 = part_one()
    res2 = part_two()

    print(
        "Answers"
        "-------"
        f"\nPart One: {res1}"
        f"\nPart Two: {res2}"
    )
