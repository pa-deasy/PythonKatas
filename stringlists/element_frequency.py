def k_most_frequency(k: int, elements: list[str]) -> list[str]:
    elements_count: dict[str, int] = {}
    
    for element in elements:
        if elements_count.get(element):
            elements_count[element] = elements_count.get(element) + 1
        else:
            elements_count[element] = 1
            
    sorted_elements_count = dict(sorted(elements_count.items(), key=lambda e: e[1], reverse=True))
    
    return list(sorted_elements_count.keys())[:k]
