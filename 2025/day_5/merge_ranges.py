def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Merges overlapping ranges in a list of (low, high) tuples.
    """

    ranges = sorted(ranges)  # prefer this over .sort() to avoid mutating input

    current_low, current_high = ranges[0]
    new = []

    for rng in ranges[1:]:
        low, high = rng  # comparison standards

        if current_high >= low:  # * overlap
            # set higher to whatever is... higher
            current_high = max(current_high, high)

        else:  # * no overlap
            # push the interval (no more merges)
            new.append((current_low, current_high))
            current_low, current_high = low, high  # start new interval for comparison

    # finally append the last interval
    new.append((current_low, current_high))
    return new
