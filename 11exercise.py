new = list(range(1,101))

for index, val in  enumerate(new):
    if val%3 == 0 and val%5 == 0:
        new[index] = "BitMaker"
    elif val%3 == 0:
        new[index] = "Bit"
    elif val%5 == 0:
        new[index] = "Maker"

print(new)
