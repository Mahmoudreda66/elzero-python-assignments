username = input('Enter Your Name\n').strip().capitalize()

print(f"Hello {username}, Happy To See You Here.")

##################################################### 2

age = int(input('Enter Your Age\n').strip())

print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" if age < 16 else f"Hello Your Age Is {age}, All Articles Is Suitable For You")

##################################################### 3

fname = input("Enter First Name\n").strip().capitalize()

lname = input("Enter Last Name\n").strip().capitalize()

print("Hello {} {:.1s}.".format(fname, lname))

##################################################### 4

email = input('Enter Your Email\n').strip()

print(f'Your Name Is {email[:email.index("@")].capitalize()}')
print(f'Email Service Provider Is {email[email.index("@") + 1:email.index(".")].lower()}')
print(f'Top Level Domain Is {email[email.index(".") + 1:].lower()}')