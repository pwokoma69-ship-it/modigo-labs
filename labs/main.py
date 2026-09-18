def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda interval: interval)
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged
    # TODO: merge overlapping or touching intervals into consolidated ranges,
    # returned sorted by start value
    pass