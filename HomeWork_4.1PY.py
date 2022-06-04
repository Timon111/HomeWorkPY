# 4. Определить, какое число в массиве встречается чаще всего.

import random
import time

r = [random.randint(0, 99) for _ in range(50)]
print(f'Массив: {r}')

begin = time.perf_counter()

max_index = 0
for i in r:
    if r.count(max_index) < r.count(i):
        max_index = r.index(i)

end = time.perf_counter()

print(f'Число {r[max_index]}, встречается {r.count(max_index)} раза')
print('Выполнено за ', end - begin)

# 2
a = [random.randint(0, 99) for _ in range(50)]
print(a)

r2 = set(a)

begin = time.perf_counter()

most_common = None
qty_most_common = 0

for i in r2:
    qty = a.count(i)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = i

end = time.perf_counter()

print(most_common)
print('Выполнено за ', end - begin)