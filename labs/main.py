def has_conflict(meetings):
    for i in range(len(meetings)):
        start1, end1 = meetings[i]
        for j in range(1 + i, len(meetings)):
            start2, end2 = meetings[j]
            if start1 < end2 and start2 < end1:
                return True
    return False

    # TODO: return True if any two meetings overlap in time, False otherwise
    pass