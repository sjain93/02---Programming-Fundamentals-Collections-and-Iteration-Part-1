print("How many Pizzas do you want to order")
quantity = int(input())

total_pizzas = list(range(1, quantity+1))
# print(total_pizzas)
for val in total_pizzas:
    toppings = []
    print("How many toppings do you want in pizza {}".format(val))
    num_pi = int(input())
    toppings.append(num_pi)
    for arg in toppings:
        print("You have ordered a pizza with {} toppings".format(arg))
