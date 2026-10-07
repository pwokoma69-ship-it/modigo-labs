def filter_and_group(catalog, required_tags, excluded_tags):
    result = {}

    for product in catalog:
        tags = product["tags"]
        if required_tags.issubset(tags) and tags.isdisjoint(excluded_tags):
            category = product["category"]
            result.setdefault(category, []).append(product["name"])
    return result
        
        

    # TODO: filter `catalog` by required_tags (must have all) and excluded_tags
    # (must have none), then group matching product names by category
    pass