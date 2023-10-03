my_list = [1, 2, 3, 3, 4, 5, 1]

unique_list = set(my_list)

print(unique_list)

unique_list = list(unique_list)

print(type(unique_list))

unique_list.pop()

print(unique_list)

##################################################### 2

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums.union(letters))

print(letters.union(nums))

nums.update(letters)

print(nums)

##################################################### 3

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)

my_set.clear()

print(my_set)

my_set.add('A')
my_set.add('B')

my_set.discard('C')

##################################################### 4

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

##################################################### 5

dic = {
    "HTML": "80%",
    "CSS": "20%",
    "PHP": "90%"
}

print(f'HTML PROGRESS IS {dic.get("HTML")}')
print(f'CSS PROGRESS IS {dic.get("CSS")}')
print(f'PHP PROGRESS IS {dic.get("PHP")}')