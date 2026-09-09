def compare_hobbies(person1_hobbies, person2_hobbies):
    return {
        "shared": person1_hobbies & person2_hobbies,
        "only_person1": person1_hobbies - person2_hobbies,
        "only_person2": person2_hobbies - person1_hobbies
    }
    # TODO: use set operations to find shared, only_person1, and only_person2 hobbies
    pass