from exercise import *
from exercise6 import *
# #1
counter = 0
while counter <=20:
    print("I will not skateboard in the halls")
    counter += 1
#
# #2
lesson = list(range(0,21))
for val in lesson:
    counter = 0
    while counter <=20:
        lesson[val] = "I will not skateboard in the halls"
        counter += 1

print(lesson)
#
# #3
num_list = list(range(1, 51))
#
# #4
total = 0
for val in num_list:
    total = total + val

print(total)
#
# #5
hola = (num_list*3)
print(sorted(hola))

#6
listB = []
listC = []
for index, country in enumerate(countries):
    if country['Island'] == False:
        listC.append(country['Country'])
    else:
        listB.append(country['Country'])
