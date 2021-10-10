# 592f2813a2bf4491fa41c3409ede7ce1
from SimpleQIWI import *

token = input('Токен: ')
phone = input('Номер кошелька: ')
api = QApi(token=token, phone=phone)

print('Выберите функцию: ')
print('[1] - Баланс счета')
print('[2] - Вывод денег')
vvod = input("")


def info():
    print('Кошелек найден!')
    print('Баланс клиента с номером', phone, 'равен: ', api.balance)


def vanish():
    summ = input('Введите сумму: ')
    num = input('Номер кошелька: ')
    try:
        api.pay(account = str(num), amount = int(summ), comment = ' ') #Вывод денег,
        print('Баланс клиента с номером', phone, 'равен: ', api.balance)
    except QIWIAPIError:
        print("Ошибка 1. Невозможно осуществить платеж самому себе.")


if vvod == "1":
    info()
elif vvod == "2":
    vanish()
else:
    quit
