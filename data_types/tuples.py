numbers = (10, 20, 30, 40, 50)
print(numbers)
print(numbers[0])
print(numbers[-1])

person = ("Talha", 25, "Software Engineer")
# person[1] = 27

name, age, profession = person
print(name)
print(profession)

num = (10, 20, 10, 30, 10, 40)
print(num.count(10))
print(num.index(30))


students = (
    ("Ali", 80),
    ("Ahmed", 90),
    ("Sara", 95)
)

student = students
print(student[0])

a = (10)
b = (10,)
print(type(a))
print(type(b))