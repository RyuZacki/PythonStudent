from typing import Any
import module

print(module.add(50, 31))

list = [3, 5, 6, 7, 1, 23, 2455, 654, 574, 74, 2, 1, 2]
fof  = {
   'Дота' : 'Гавно',
    54 : 228,
   'Корона' : 'Вирус',
    2020 : 3020
}
hai = (3, 4, 3, 32, 68, 43, 8, 0, 65 ,90 ,5, 7)

sqs = {1:3, 2:6, 3:45, 4:63, 5:3, 6:90, 7:28, 8:19, 9:9, 10:0}

print( list[::-1])
print( list[3:7])

x = int(input('Введите число: '))
if x in sqs:
    b = x + 1
    print('Число {0} и {1}'.format(sqs[x], sqs[b]))
else:
    print('Пуся')


def sum(a, b):
    c = a + b
    print('Сумма чисел ' + str(a) + ' и ' + str(b) + ' равна: ' + str(c))

a = int(input('Число 1: '))
b = int(input('Число 2: '))
sum(a, b)

print('Data' * 4)