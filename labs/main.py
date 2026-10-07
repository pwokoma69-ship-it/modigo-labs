def count_cheap_rides(fares, limit):
    """
    Counts how many fares in the list are strictly less than `limit`.
    Returns the count as an integer.
    """
    count = 0  # TODO: this should start at zero — is this right?

    for fare in fares:
        if fare < limit:  # TODO: check the condition — should this compare fare to limit?
            count += 1  # TODO: this line doesn't actually do anything — fix it so count goes up by 1

    return count  # TODO: make sure this returns the right variable