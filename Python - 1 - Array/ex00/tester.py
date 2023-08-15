from give_bmi import give_bmi, apply_limit


height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi), type(bmi[0]))
apply = apply_limit(bmi, 26)
print(apply, type(apply), type(apply[0]))
