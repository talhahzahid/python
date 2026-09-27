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

text = 'helloworld'
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
