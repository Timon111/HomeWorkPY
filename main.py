# задание 1

# m = int(input('Введите трехзначное число - '))
# if m > 999 or m < 99:
#     print("ОШИБКА ВВОДА")
# a = m % 10
# b = int((m % 100 - a) / 10)
# c = int((m - m % 100) / 100)
# print("сумма - " and a + b +c)
# print("произведение - " and a * b * c)

# задание 2

#print((5 and 6))
#print((5 or 6))
#print((not 5))
#print((not 6))
#print((5 << 2)) # умножение на 2 каждый сдвиг на 1
#print((5 >> 2)) # деление на 2 целочисленное

# задание 3

# x1 = int(input())
# x2 = int(input())
# y1 = int(input())
# y2 = int(input())
# k = (y1 - y2) / (x1 - x2)
# b = y2 - k * x2
# print("y = " + str(k) + " * x + " + str(b))

# задание 4

import random
# a = int(input())
# b = int(input())
# print(random.randint(a,b))

# c = float(input())
# d = float(input())
# print(random.uniform(c,d))

# alf = []
# for i in range(65,91):
#     alf.append(chr(i))
# print(random.choice(alf))

# задание 5 и 6

# a = ord(input("1-я буква: "))
# b = ord(input("2-я буква: "))
# a = a - ord("a") + 1
# b = b - ord("a") + 1
# print("Позиции: %d и %d" % (a,b))
# print("Между буквами символов:", abs(a-b)-1)
#
# n = int(input("Номер буквы в алфавите: "))
# n = ord("a") + n - 1
# print("Это буква", chr(n))

# задание 7

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a + b <= c or a + c <= b or b + c <= a:
#     print("Треугольник не существует")
# elif a != b and a != c and b != c:
#     print("Разносторонний")
# elif a == b == c:
#     print("Равносторонний")
# else:
#     print("Равнобедренный")

# задание 8

# x = int(input())
# if (x % 4) == 0:
#     print(chr(x) + " високосный год")
# else:
#     print(chr(x) + " не високосный год")

# задание 9

# a = int(input())
# b = int(input())
# c = int(input())
# if ((a < b) and (b < c)) or ((c < b) and (b < a)):
#     print(b)
# elif ((b < a) and (a < c)) or ((c < a) and (a < b)):
#     print(a)
# elif ((a < c) and (c < b)) or ((b < c) and (c < a)):
#     print(c)
# else:
#     print("такой цифры нет")