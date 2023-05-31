# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и 
# не больше заданного максимума)

import random

list = [random.randint(-10, 11) for _ in range(15)]

print(list)

min_list = 0
max_list = max(list)

for (i, elem) in enumerate(list):
    if min_list < elem < max_list:
        print(i, end = ' ')

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] 
# min_number = int(input()) 
# max_number = int(input()) 
# for i in range(len(list_1)):   
#     if min_number <= list_1[i] <= max_number:     
#         print(i)

# for i in range(len(list)):
#     if min_list < list[i] < max_list:
#         print(i, end = ' ')