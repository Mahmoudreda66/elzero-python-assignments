name = 'Elzero'
age = '19'
country = 'Egypt'

print("Hello '" + name + "', How You Doing \\ \"\"\" Your Age Is \"" + age + "\"\" + And Your Country Is: " + country)

##################################################### 2

print("""
"Hello '""" + name + """', How You Doing \\
\"\"\" Your Age Is \"""" + age + """\"\" +
And Your Country Is: """ + country)

##################################################### 3

print(name[1:2])
print(name[2:3])
print(name[-1])

##################################################### 4

print(name[1:4])
print(name[::2])
print(name[-2::-2])

##################################################### 5

name = "#@#@Elzero#@#@"

print(name.strip('#@'));

##################################################### 6

num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

##################################################### 7

name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, '@'))
print(name_two.rjust(20, '@'))

##################################################### 8

name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

##################################################### 9

msg = "I Love Python And Although Love Elzero Web School"

print(msg.find('Love'))

##################################################### 10

name = "Elzero"

print(name.index('z'))

##################################################### 11

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace('<3', 'Love', 1))

##################################################### 12

print(msg.replace('<3', 'Love'))

##################################################### 13

name = "Osama"
age = 38
country = "Egypt"

print('My Name Is {}, And My Age Is {}, And My Coutry Is {}'.format(name, age, country))