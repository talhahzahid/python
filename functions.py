def square(number):
    return number**2


result = square(4)
print(result)


def add(num1, num2):
    return num1 + num2


print(add(1, 2))


def multiply(p1, p2):
    return p1 + p2


print(multiply(1, 2))

import math


def circle_stats(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference


print(circle_stats(3))
