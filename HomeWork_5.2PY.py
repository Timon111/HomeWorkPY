# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict
from collections import deque

# перевод в 10-чную
def in_ten(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def in_sixteen(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in signs:
    table[key] += counter
    counter += 1

num_1 = in_ten(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
num_2 = in_ten(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел: {in_sixteen(num_1 + num_2)}')
print(f'Произведение чисел: {in_sixteen(num_1 * num_2)}')