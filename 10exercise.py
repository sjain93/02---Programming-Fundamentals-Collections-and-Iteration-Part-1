students = {
  'cohort1': 34,
  'cohort2': 42,
  'cohort3': 22
}

for key, value in students.items():
    print("{}:{}".format(key, value))

students['cohort4'] = 43

for key in students.keys():
    print("{}".format(key))


print(students)

for key, value in students.items():
    students[key] = 1.05* value

students.pop('cohort2')
print(students)

def sumFunc(num_list = []):
    total = 0
    for val in num_list:
        total = total + val
    return total

current_students = list(students.values())
print(sumFunc(current_students))
