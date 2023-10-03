num1 = float(input('Number One:\n').strip())
num2 = float(input('Number Two:\n').strip())

operation = input('Operation: (+, -, *, /):\n').strip()

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print('Unsupported Operation')

##################################################### 2

age = int(input('Enter Your Age\n').strip())

print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")

##################################################### 3

age = int(input('Enter Your Age\n').strip())

if age < 10 or age > 100:
    print('Usupported Age')
else:
    print(f"Months: {age * 12}")
    print(f"Weeks: {age * 48}")
    print(f"Days: {age * 365}")
    print(f"Hours: {age * 12 * 30 * 24}")
    print(f"Minutes: {age * 12 * 30 * 24 * 60}")
    print(f"Seconds: {age * 12 * 30 * 24 * 60 * 60}")

##################################################### 4

country = input("Input Your Country\n").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")