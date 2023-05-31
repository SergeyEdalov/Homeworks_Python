# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input('Enter coins count: '))
count_zero = 0
count_one = 0
text = 'Минимальное кол-во монет, которые нужно перевернуть:'

for i in range(1, n + 1):
    i = random.randint(0,1)
    if i == 0:
        count_zero += 1
    else:
        count_one += 1

    print(i, end=' ')

if count_zero > count_one: print('\n', count_one)
else: print('\n', text, count_zero)



# for i in range(n):
#     if i == 0:
#         count +=1
# if count < n / 2:
#     print(count)
