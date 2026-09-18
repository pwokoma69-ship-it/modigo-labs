def has_conflict(meetings):
    for p in range(len(meetings)):
        start1, end1 = meetings[p]
        for w in range(1 + p, len(meetings)):
            start2, end2 = meetings[w]
            
            if start1 < end2 and start2 < end1:
                return True
    return False
    # TODO: return True if any two meetings overlap in time, False otherwise
    pass