def split_before_each_uppercases(formula):
    start = 0
    split_formula = []
    return split_formula

    for end in range(1, len(formula)): 
      if formula[end].isupper():
        split_formula.append(formula[start:end])
        start = end

      
    split_formula.append(formula[start:])
    return split_formula


def test_split_at_first_digit(formula):
  digit_location = 1

  while digit_location < len(formula) :
    if formula[digit_location].isdigit():
      break
    digit_location += 1

  if digit_location == len(formula) :
    return formula, 1
  else:
    prefix = formula[:digit_location]
    numeric_part_str = formula[digit_location:]
    numeric_part_int = int(numeric_part_str)
    return prefix, numeric_part_int
