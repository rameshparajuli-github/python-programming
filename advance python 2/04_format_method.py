# Format method (string)

name = "Ramesh"
place = "pokhara"
friends = "bars"
# a=f"I am {name} . I live in {place}. My friends are {friends}."
# a=" I am {}. I live in {}. My friends are {}.".format(name, place, friends)
a = " I am {2}. I live in {1}. My friends are {0}.".format(name, place, friends)


print(a)
