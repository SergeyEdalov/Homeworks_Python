# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# ЧЕРЕЗ МАТЕМАТИКУ
# import random
# import math

# S = int(input('Введите сумму чисел: '))
# P = int(input('Введите произведение чисел: '))

# D = S * S - 4 * P
# print(D)
# Y = (S + math.sqrt(D)) / 2
# X = S - Y

# print('Числа: ', X, Y)

# ЧЕРЕЗ ЦИКЛЫ

x = int(input()) 
y = int(input()) 
for i in range(x):     
    for j in range(y):         
        if x == i + j and y == i * j:             
            print(i, j)