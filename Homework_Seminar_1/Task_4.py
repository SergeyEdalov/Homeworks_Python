# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no


m = int(input('Введите размер длины шоколадки: '))
n = int(input('Введите размер ширины шоколадки: '))
k = int(input('Введите кол-во необходимых долек: '))

if m * n <= k:
    print('Кол-во необходимых долек меньше шоколадки или разлом не требуется')
else:
    if k % m == 0 or k % n == 0:
        print('Да, можно разломить')
    else:
        print('Нет, нельзя разломить')