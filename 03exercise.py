from exercise import *

for i in fav_artists:
    print("I think {} is a great band".format(i))

print(fav_artists[0], ",", fav_artists[1])

for film, release in movies.items():
    print("{} came out in {}".format(film, release))

new = list(reversed(list(sorted(friend_age))))
print(new)

movies['Beauty and the Beast'] = [1991, 2017]
print(movies)
