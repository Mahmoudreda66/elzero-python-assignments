print(bool(True))
print(bool(100))
print(bool("Mahmoud"))
print(bool(["Hello", "World"]))

print(bool(not True)) # False
print(bool(0))
print(bool(""))
print(bool([]))

##################################################### 2

html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)

##################################################### 3

num_one = 10
num_two = 20
num = 20

print(num > num_two or num > num_one)
print(num > num_two and num > num_one)

##################################################### 4

num_one = 10
num_two = 20

result = num_one + num_two

print(result)

exp_3 = result ** 3

print(exp_3)

division = exp_3 % 26000

print(division)

print((division) / 5)

print(type(str((division) / 5)))