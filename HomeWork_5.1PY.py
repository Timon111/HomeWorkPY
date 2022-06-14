# 1. Пользователь вводит данные
# о количестве предприятий,
# их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections

n = int(input('Введите количество компаний: '))

companies = collections.defaultdict()
above = collections.deque()
below = collections.deque()
all_profit = 0
QUARTER = 4

for i in range(n):
    name = input(f'\nВведите название {i+1}й компании: ')
    profit = 0
    q = 1
    while q <= QUARTER:
        profit += float(input(f'Введите прибыль за {q}й квартал: '))
        q += 1
    companies[name] = profit
    all_profit += profit

mid_profit = all_profit / n

for i, item in companies.items():
    if item >= mid_profit:
        above.append(i)
    else:
        below.append(i)

print(f'Средняя прибыль для всех компаний составила: {mid_profit}')

print(f'Прибыль выше среднего у {len(above)} компаний:')
for name in above:
    print(name)

print(f'Прибыль ниже среднего у {len(below)} компаний:')
for name in below:
    print(name)