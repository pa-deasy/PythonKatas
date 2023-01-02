def longest_increasing_subsequence_from(numbers: list[int]) -> int:
    calculations: list[int] = []
    
    for index in range(0, len(numbers)):
        calculations.append(1)
        
        
    longest_sequence = 1 
    for fixed_index in range(1, len(calculations)):
        for compared_index in range(0, fixed_index):
            if numbers[fixed_index] > numbers[compared_index] and calculations[compared_index] + 1 > calculations[fixed_index]:
                sequence = calculations[compared_index] + 1
                calculations[fixed_index] = sequence
                
                if sequence > longest_sequence:
                    longest_sequence = sequence
            
            compared_index += 1
            
        fixed_index += 1
    
    
    return longest_sequence
