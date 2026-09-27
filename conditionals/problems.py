# userscore = int(input("Give me a score value: "))

# 1
age = 27
# age = int(input('Enter your age: '))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenagers")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# 2
userage = 22
day = "Wednesday"

price = 12 if userage >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Ticket price is $",price)
