from collections import Counter

dies = [1, 1, 1, 3, 1, 3, 1, 4, 3, 5, 5]
#{i:dies.count(i) for i in set(dies)}

dies_in_dict = dict(Counter(dies))
print("Currect dies:", dies)
print("Dies via dictionary:", dies_in_dict) 
result = 0
for current_value in dies_in_dict:
    print ("Current value: ", current_value, " Times: ", dies_in_dict[current_value])
    if dies_in_dict[current_value] >= 3:
        combo_count = dies_in_dict[current_value] // 3
        print("  Value", current_value, "has", combo_count, "combos. P.S. Combo is value 3 times" )
        if current_value == 1:
            result += 1000*combo_count
        else:
            result += current_value*100*combo_count
        print("    Current result is", result )
        dies_in_dict[current_value] = dies_in_dict[current_value] - 3*combo_count
    if current_value == 1:
        result += 100*dies_in_dict[current_value]
        print("  Value is ", current_value, ". need to do some math here" )
        print("    Current result is", result )
    if current_value == 5:
        result += 50*dies_in_dict[current_value]
        print("  Value is ", current_value, ". need to do some math here" )
        print("    Current result is", result )

print("Final result:", result)


