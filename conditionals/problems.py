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

print("Ticket price is $", price)


score = 98
if score >= 101:
    print("Enter Correct Score bellow 100 or 100")
    exit()

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("F")


fruite = "Banana"
color = "yellow"

if fruite == "Banana":
    if color == "yellow":
        print("Ripe")
    elif color == "green":
        print("UnRipe")
    elif color == "brown":
        print("OverRipe")


weather = "Snowy"
if weather == "Sunny":
    print("Go for a walk")
elif weather == "Rainy":
    print("Read a book")
elif weather == "Snowy":
    print("Build a snowman")


distance = 5

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("AI recommends you the transport of: ", transport)


order_size = "Medium"
extrashot = False

if extrashot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print(coffee)


password = "Secure3P@ss"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is: ", strength)


year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, " is a leap year")
else:
    print(year, "is NOT a leap year")


species = input("Enter pet species: ")
pet_age = int(input("Enter pet pet_age: "))

if species == "Dog":
    if pet_age < 2:
        print("Puppy food")
    else:
        print("Adult dog food")

elif species == "Cat":
    if pet_age < 1:
        print("Kitten food")
    elif pet_age > 5:
        print("Senior cat food")
    else:
        print("Adult cat food")

else:
    print("Unknown pet species")
