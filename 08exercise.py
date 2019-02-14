
def sumFunc(num_list = []):
    total = 0
    for val in num_list:
        total = total + val
    return total

test_list = [1.5,221,32,46,51]

print(sumFunc(test_list))
