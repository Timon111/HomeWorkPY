# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе
# символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

# def operations(a, b, operator):
#     if operator == '+':
#         return a + b
#     elif operator == '-':
#         return a - b
#     elif operator == '*':
#         return a * b
#     else:
#         return a / b
#
#
# def check(operator):
#     return operator == '0' or operator == '+' or operator == '-' or operator == '*' or operator == '/'
#
#
# def get_operator():
#     return input('Оператор: ')
#
#
# def first_exersice(a=None, b=None):
#     if a is None:
#         a = float(input('a: '))
#     if b is None:
#         b = float(input('b: '))
#     operator = get_operator()
#
#     if not check(operator):
#         print('Неверный оператор')
#         first_exersice(a, b)
#         return
#     elif operator == '0':
#         return
#     elif operator == '/' and b == 0:
#         print('No division by zero')
#         first_exersice()
#         return
#     else:
#         print(operations(a, b, operator))
#         first_exersice()
#
#
# first_exersice()

# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# import math
#
# x = int(input('Введите число: '))
#
# odd = 0 # Нечетн
# even = 0 # Четн
#
#
# def last_odd_or_even(x):
#   global odd, even
#   last_digit = x % 10
#   if last_digit % 2 == 0:
#     even += 1
#   else:
#     odd += 1
#
#
# last_odd_or_even(x)
#
# while x >= 10:
#   x = math.floor(x / 10)
#   last_odd_or_even(x)
#
# print('Нечетные:', odd)
# print('Четные:', even)

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# import math
#
# x = int(input('Введите число: '))
#
# reverse = ""
#
#
# def add_last_digit(x):
#   global reverse
#   last_digit = x % 10
#   reverse = reverse + str(last_digit)
#
#
# add_last_digit(x)
#
# while x >= 10:
#   x = math.floor(x / 10) # floor округление числа в меньшую сторону
#   add_last_digit(x)
#
# print('Слово наоборот:', int(reverse))

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

# n = int(input('Введите n количество элементов: '))
#
# if n == 0:
#   print('Сумма равна = :', 0)
#   exit()
#
# m = 1
#
# for i in range(1, n):
#   if i % 2 == 0:
#     m += 1 / (2**i)
#   else:
#     m += 1 / -(2**i)
#
# print('Сумма элементов последовательности равна = :', m)

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

# for i in range(32,128):
#     print('%4d-%s' % (i, chr(i)), end=' ')
#     if i%10 == 0:
#         print()

# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

# import random
#
# rand_num = random.randrange(0, 100)
#
# for i in range(10, 0, -1):
#   x = int(input('Ваша догадка: '))
#   if x == rand_num:
#     print('Вы угадали!')
#     exit()
#   elif x < rand_num:
#     print('Слишком мало')
#   else:
#     print('Слишком много')
#
# print('Вы проиграли. Правильный ответ был: ', rand_num)

# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


# def _current_num(n):
#     return n * (n + 1) / 2
#
#
# def _next_num(n):
#     return (n + 1) * (n + 2) / 2
#
#
# for i in range(1000):
#     print(_current_num(i + 1) == _next_num(i))

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# from functools import reduce
#
# number = input('Введите цифру: ')[0]
# sequence = input('Введите последовательность: ')
# print('Цифра {} встречается {} раз(a)'.format(number, reduce(lambda acc, x: acc + int(x == number), sequence, 0)))

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# from functools import reduce
#
#
# def summary(string):
#     return reduce(lambda acc, x: acc + int(x), string, 0)
#
#
# def more(a, b):
#     return a if summary(a) > summary(b) else b
#
#
# numbers = input('Введите числа одной строкой через пробелы: ').split()
# first = (numbers or [None])[0]
# print('Наибольшее по сумме цифр {}'.format(reduce(lambda maximal, x: more(x, maximal), numbers, first)))