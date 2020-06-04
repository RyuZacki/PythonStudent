list1 = list(range(6, 200, 2))
print(list1)
list1.append(200)
list1.insert(5, 222)
list1.remove(30)

if 30 not in list1:
    print("Числа 30 нету")
    if 200 and 222 in list1:
        print("Число 200 и 222 есть!")


def f1():
    try:
        a = int(input('Введите число: '))
        return a
    except ValueError:
        print("Вы ввели не то значение!")
        return None


while True:
    a = f1()
    if a is not None:

        if a % 2 == 0:
            print("Это число четное!")
        else:
            print("Это число нечетное!")

        D = str(input("Желаете продолжить? Y/N "))

        if D == 'Y':
            continue
        if D == 'N':
            break


#
# class H1():
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#         print('1')
#
#     def n(self):
#         print(self.name)
#
# H = input('Введите ... ')
# W = input('Введите ... ')
# N = input('Введите ... ')
# A = input('Введите ... ')
#
# players = []
#
# player = H1(H, W, N, A)
# print(player.age)
# player.n()
# print(players)