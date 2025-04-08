def reverse_sentence(sentence: str) -> str:
    words = sentence.split()
    reversed_sentence = ''
    
    for word in words:
        if not reversed_sentence:
            reversed_sentence = word
        else:
            reversed_sentence = f'{word} {reversed_sentence}'
            
    return reversed_sentence


def another_reverse_sentence(sentence: str) -> str:
    chars = list(sentence)
    reversed_sentence = ''
    current_word = ''
    
    while chars:
        char = chars.pop()
        
        if char == ' ':
            reversed_sentence = f'{reversed_sentence} {current_word}'
            current_word = ''
        else:
            current_word = char + current_word
            
    reversed_sentence = f'{reversed_sentence} {current_word}'
    
    return reversed_sentence.strip()


def efficient_reverse_sentence(sentence: str) -> str:
    words = sentence.split()

    left_index = 0
    right_index = len(words) - 1

    while left_index < right_index:
        words[left_index], words[right_index] = words[right_index], words[left_index]
        left_index += 1
        right_index -= 1

    return ' '.join(words)
