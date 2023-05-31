# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
size_list_1 = int(input('Введите размер первого списка: '))
size_list_2 = int(input('Введите размер второго списка: '))

list_1 = [random.randint(0, 10) for _ in range(0, size_list_1)]
list_2 = [random.randint(0, 10) for _ in range(0, size_list_2)]

print(list_1)
print(list_2)

list_3 = []

for i in list_1:
    for j in list_2:
        if i == j:
            list_3.append(i)

list_3 = set(list_3)
print(list_3)





