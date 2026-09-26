# user = {
#     "username":"john",
#     "age":12,
#     "city":"karachi"
# }
# print(user)
# user["username"] = 'talha'
# print(user["username"])


student = {
    "name": "Ali",
    "age": 15,
    "grade": "A",
    # "city": "Karachi"
}

print(student)
student["grade"] = "B"
student["city"] = "Karachi"
print(student)

car = {"brand": "Toyota", "model": "Corolla", "year": 2020, "color": "white"}

del car["color"]
print(car)

person = {"name": "John", "age": 20, "city": "Lahore", "job": "Developer"}
print(len(person))

user = {"username": "john", "age": 20, "city": "Karachi"}

if "age" in user:
    print("yes age is exits")


fruits = {"apple": 5, "banana": 10, "orange": 7}

for key, value in fruits.items():
    print(key, value)


prices = {"apple": 100, "banana": 50, "orange": 80}

total = 0
for cal in prices:
    print(prices[cal])
    total += prices[cal]


print(total)


marks = {"Ali": 75, "Ahmed": 92, "Sara": 88, "John": 67}

highest = 0
for val in marks:
    if marks[val] > highest:
        highest = marks[val]


print(highest)


students = {"Ali": 85, "Ahmed": 72, "Sara": 95, "John": 68}

for stud in students:
    if students[stud] >= 80:
        print(stud, students[stud])


words = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
