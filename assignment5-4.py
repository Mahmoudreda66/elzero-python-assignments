myTuple = "Mahmoud",

print(myTuple[0])
print(type(myTuple))

##################################################### 2

friends = ("Osama", "Ahmed", "Sayed")

friends = list(friends)

friends[0] = "Elzero"

friends = tuple(friends)

print(friends)
print(type(friends))
print("{} Elements".format(len(friends)))

##################################################### 3

nums = (1, 2, 3)
letters = ("A", "B", "C")

total = nums + letters

print(total)
print(len(total))

##################################################### 4

my_tuple = (1, 2, 3, 4)

a, b, d, c = my_tuple

print(a)
print(b)
print(c)