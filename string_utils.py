def split_before_each_uppercases(formula):
    start = 0
    split_formula = []
    
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i
            
    split_formula.append(formula[start:])
    return split_formula



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
