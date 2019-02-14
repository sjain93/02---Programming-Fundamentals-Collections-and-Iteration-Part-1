def output(groclist = []):
    for elem in grocery_list:
        print("*{}".format(elem))

def newitem(item, grocelist = []):
    grocelist.append(str(item))
    output(grocelist)

def foodcheck(item, grocelist = []):
    if item not in grocelist:
        print("You need to pick up {} today".format(item))
    else:
        print("You don't need to pick up {} today.".format(item))

grocery_list = ["carrots", "toilet paper", "apples", "salmon"]

newitem('bread',grocery_list)
print(grocery_list)

total_items = len(grocery_list)
print(total_items)

foodcheck('bananas', grocery_list)
foodcheck('apples', grocery_list)

#9.4
print(grocery_list[1])

#9.5
grocery_list.sort()
output(grocery_list)

#9.6
grocery_list.pop(grocery_list.index('salmon'))
output(grocery_list)
