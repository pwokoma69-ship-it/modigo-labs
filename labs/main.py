def top_words(text, n):
    if not text:
        return []
    
    counts = {}
    for word in text.split():
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:n]
    
    
    
    # TODO: count word frequency (case-insensitive), then return the top `n`
    # as (word, count) tuples sorted by count descending, ties broken alphabetically
    pass