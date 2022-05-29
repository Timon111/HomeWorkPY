# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# count = {}
# for n in range(2, 10):
#     count[n] = []  # отчищаем словарь
#     for f in range(2, 100):
#         if f % n == 0:  # определяем кратность
#             count[n].append(f)  # если кратно то добавляем в словарь
#     print(f'Для числа {n} кратны - {len(count[n])}. Кратные числа: {count[n]}.')

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

# import random
#
# r = [random.randint(0, 99) for _ in range(10)]  # создаю массив из 10 элементов заполненный рандомными числами
# print(f'Первый массив {r}')  # вывожу массив
# new_ar = []  # второй пустой массив для индексов
#
# for n in r:
#     if n % 2 == 0:
#         new_ar.append(r.index(n))  # добавляю в новый массив индексы четных элементов
#
# print(f'Индексы чётных элементов первого массива: {new_ar}')  # вывожу второй массив

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# import random
#
# r = [random.randint(0, 99) for _ in range(10)]
# print(f'Массив начальный: {r}')
#
# max = r[0]
# min = r[0]
#
# for i in r:  # перебираем элементы в массиве r
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# min_index = r.index(min)
# max_index = r.index(max)
# r[min_index], r[max_index] = r[max_index], r[min_index]  # меняем местами элементы
# print(f'Массив осле изменения: {r}')

# 4. Определить, какое число в массиве встречается чаще всего.

# import random
#
# r = [random.randint(0, 99) for _ in range(100)]
# print(f'Массив: {r}')
#
# max_index = 0
# for i in r:
#     if r.count(max_index) < r.count(i):
#         max_index = r.index(i)
#
# print(f'Число {r[max_index]}, встречается {r.count(max_index)} раза')

# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

# import random
#
# r = [random.randint(-99, 99) for _ in range(50)]
# print(f'{r}')
# min_index = 0
#
# for i in r:
#     if r[min_index] > i:
#         min_index = r.index(i)
#
# if r[min_index] >= 0:
#     print(f'В массиве нет отрицательных элементов')
# else:
#     print(f'Минимальный отрицательный элемент: {r[min_index]}.',
#             f'Индекс элемента {min_index}')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# import random
#
# r = [random.randint(0, 99) for _ in range(10)]
# print(f'Массив: {r}')
#
# min_index = 0
# max_index = 0
# step = 1
# sum = 0  # сумма элементов между минимальным и максимальным элементами
#
# for i in r:
#     if r[min_index] > i:
#         min_index = r.index(i)
#     elif r[max_index] < i:
#         max_index = r.index(i)
#
# if max_index - min_index < 0:
#     step = -1
#
# for i in r[min_index + step:max_index:step]:
#     sum += i
#
# print(f'Сумма элементов между минимальным ({r[min_index]})', f' и максимальным ({r[max_index]}) элементами: {sum}')

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# import random
#
# r = [random.randint(0, 99) for _ in range(50)]
# print(f'Массив: {r}')
#
# sort_list = []  # создаем пустой список для отсортированного r
# sort_list.extend(r)  # заполняем новый список начальным
# sort_list.sort()  # сортируем по возрастанию
#
# print(f'Два наименьших элемента (второй способ): {sort_list[0]} и {sort_list[1]}')

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# str_ = 5
# coll_ = 4
# matr_ = []
# for i in range(coll_):
#     b = []
#     sum_ = 0
#     print("%d-я строка:" % i)
#     for j in range(str_-1):
#         n = int(input())
#         sum_ += n
#         b.append(n)
#     b.append(sum_)
#     matr_.append(b)
#
# for i in matr_:
#     print(i)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# import random
#
# matrix = []
#
# for i in range(5):
#     matrix.append([])
#     matrix[i].extend([random.randint(0, 50) for _ in range(5)])
#
# min_list = []  # список с минимальными элементами столбцов
# min_list.extend(matrix[0])
#
# for string in matrix:
#     print()
#     print(('{:4d} ' * len(string)).format(*string))
#     i = 0
#     for j in string:
#         if j < min_list[i]:
#             min_list[i] = j
#         i += 1
#
# print()
# print('Список с минимальными элементами столбцов')
# print(('{:4d} ' * len(min_list)).format(*min_list))
# print()
#
# min_list.sort(reverse=True)  # сортируем по убыванию
# print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', min_list[0])
