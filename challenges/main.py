def dedupe_preserve_order(items):
    total = []
    for item in items:
        if item not in total:
            total.append(item)
    return total


    # TODO: use a set to track seen values while building a new list
    # that preserves the original order of first appearances
    pass