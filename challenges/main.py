def find_common_elements(list1, list2):
    common = []
    for item in list1:
        for value in list2:
            if item == value:
                if item not in common:
                    common.append(item)
    return common
    # TODO: use for loops to find values present in both list1 and list2, with no duplicates
    pass