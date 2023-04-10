# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket = int(input('Введите номер билета: '))

if ticket > 99999 and ticket < 1_000_000:
    m = ticket // 10
    f = ticket % 10
    e = m % 10
    n = m // 10
    d = n % 10
    i = n // 10
    c = i % 10
    j = i // 10
    b = j % 10 
    a = ticket // 100000

    if a + b + c == e + d + f:
        print ('Билет счастливый')
    else: 
        print ('Билет несчастливый')
else: print ('Билет не является шестизначным')

