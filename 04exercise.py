from exercise import *

#4.1
for val in friend_age:
    if val < 30 :
        print(val)
#4.2 Maximum age of friend_age list
print(max(friend_age))

#4.3
counter = 0
for val in coin_flip:
    if val == "H":
        counter += 1
print(counter)

#4.4
fav_artists.pop(0)
# print(fav_artists)

#4.5
cities['Toronto'] = 2732000
# print(cities)
