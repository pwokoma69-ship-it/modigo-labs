def second_largest(numbers):
    unique_numbers = set(numbers)
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)
    
    # TODO: return the second largest DISTINCT number in `numbers`
    pass