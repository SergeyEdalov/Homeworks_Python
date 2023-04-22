# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#  4 

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def summa_counts(a, b):
    if b == 0: return a
    if a == 0: return b
    if a >= b: return summa_counts(a + 1, b - 1)
    else: return summa_counts(a - 1, b + 1)
    
print(summa_counts(a, b))