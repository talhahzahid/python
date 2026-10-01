import time

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_numbers_count = 0
for num in numbers:
    if num > 0:
        positive_numbers_count += 1

print(positive_numbers_count)


sum_even = 0
for i in range(1, 11):
    if i % 2 == 0:
        sum_even += 1

print(sum_even)


for i in range(1, 11):
    if i == 5:
        continue
    print("2", "*", i, "=", i * 2)

text = "helloworld"
arr = list(text)

start = 0
end = len(arr) - 1

while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    start += 1
    end -= 1

print("".join(arr))

input_str = "helloworld"

for char in input_str:
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break


number = 5
factorial = 1

while number > 0:
    factorial = factorial * number
    number -= 1

print(factorial)

while True:
    user_num = int(input("Enter number between 1/10: "))

    if user_num >= 1 and user_num <= 10:
        print("Thanks")
        break
    else:
        print("Invalid Number")

nums = 29
is_prime = True

if nums > 1:
    for i in range(2, nums):
        if (nums % i) == 0:
            is_prime = False
            break

print(is_prime)


items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)

print(unique_item)


wait_time = 1
max_retries = 5
attempts = 0


while attempts < max_retries:
    print("Attempt", attempts + 1, "-wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
