friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0]);
print(friends[-5]);

print(friends[4]);
print(friends[-1]);

##################################################### 2

print(friends[::2])
print(friends[1::2])

##################################################### 3

print(friends[1:4])
print(friends[3:5])

##################################################### 4

friends[3:5] = ['Elzero', 'Elzero']

print(friends)

##################################################### 5

friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, 'Nasser')
print(friends)
friends.append('Salem')
print(friends)

##################################################### 6

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends[0:2] = []
print(friends)
friends.pop()
print(friends)

##################################################### 7

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)

print(friends)

##################################################### 8

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()

print(friends)

friends.sort(reverse=True)

print(friends)

##################################################### 9

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends))

##################################################### 10

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[4][0])
print(technologies[4][2])