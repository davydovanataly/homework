import math


def square(side):
    area = side * side
    return math.ceil(area)


side = float(input("Введите число: "))


result = square(side)
print(result)
