def split_before_each_uppercases(formula):
    start = 0
    end = 1
    elements_lst = []
    
    if not formula:
        return elements_lst
    
    while end < len(formula):
        if formula[end].isupper():
            elements_lst.append(formula[start:end])
            start = end
        end+=1  
        
    elements_lst.append(formula[start:])
    
    return elements_lst


def split_at_first_digit(formula):
    for char_index, char in enumerate(formula):
        if char.isdigit():
            return formula[:char_index], int(formula[char_index:])
    return formula, 1


def split_at_first_digit(formula):
    digit_location = 0
    
    while digit_location < len(formula) and not formula[digit_location].isdigit():
        digit_location += 1

    if digit_location == len(formula):
        return formula, 1
    
    num_end = digit_location
    while num_end < len(formula) and formula[num_end].isdigit():
        num_end += 1
        
    prefix = formula[:digit_location]
    numeric_part_str = formula[digit_location:num_end]
    numeric_part_int = int(numeric_part_str)
            
    return prefix, numeric_part_int
