def permutations(s: str) -> list[str]:
    return _generate_permutations(s[1:], s[:1], [])
    

def _generate_permutations(remaining: str, prefix: str, perms: list[str]) -> list[str]:
    if not remaining:
        perms.append(prefix)
        return perms
    
    remaining_post_pop = remaining[1:]
    popped_char = remaining[:1]
    
    for index in range(len(prefix) + 1):
        new_prefix = prefix[:index] + popped_char + prefix[index:]
        perms + _generate_permutations(remaining_post_pop, new_prefix, perms)
        
    return perms
        
        
    
    
    
    


# word = 'abc'
# a -> ba ab ->
# expected = ['cab', 'acb', 'abc', 'cba', 'bca', 'bac']