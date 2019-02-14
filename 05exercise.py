from exercise import *

#5.1
total_pop = sum(cities.values())

print(total_pop)

#5.2
for key, val in friends.items():
    if val > 26:
        print("{} is old".format(key))
    elif val < 26:
        print("{} is young".format(key))


#5.3
print("{}, {}".format(fav_colours[-1], fav_colours[-2]))

#5.4
for index, grade in enumerate(friend_age):
  friend_age[index] = grade + 1

print(friend_age)

#5.5
fav_colours.append("teal")
fav_colours.append("sea green")

#5.6
