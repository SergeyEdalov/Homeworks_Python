# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


n = int(input('Enter three-digit count: '))

if n > 99 and n < 1000:
    m = n // 10
    a = n // 100
    b = m % 10
    c = n % 10
    sum = a + b + c
    print('The sum of the digits of a three-digit number: ',sum)
else:
    print('The number is not a three-digit positive')


