#Определитель
cycle = True


def DeterminantOfOrder2():
    a11, a12 = int(input("Введите элеммен a11: ")), int(input("Введите элеммен a12: "))
    a21, a22 = int(input("Введите элеммен a21: ")), int(input("Введите элеммен a22: "))

    print("Определитель 2 порядка")
    print("   |{a} {b}| \n   |{a1} {b1}|".format(a=a11, b=a12, a1=a21, b1=a22))

    A = (a11 * a22) - (a12 * a21)

    print("Вычеслинный определитель {0}".format(A))


def DeterminantOfOrder3():
    a11, a12, a13 = int(input("Введите элеммен a11: ")), int(input("Введите элеммен a12: ")), int(input("Введите элеммен a13: "))
    a21, a22, a23 = int(input("Введите элеммен a21: ")), int(input("Введите элеммен a22: ")), int(input("Введите элеммен a23: "))
    a31, a32, a33 = int(input("Введите элеммен a31: ")), int(input("Введите элеммен a32: ")), int(input("Введите элеммен a33: "))

    print("Определитель 3 порядка")
    print("   |{a} {b} {c}| \n   |{a1} {b1} {c1}| \n   |{a2} {b2} {c2}|".format(a=a11, b=a12, c=a13, a1=a21, b1=a22, c1=a23, a2=a31, b2=a32, c2=a33))

    A = (a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32) - (a13 * a22 * a31) - (a11 * a23 * a32) - (a12 * a21 * a33)

    print("Вычеслинный определитель {0}".format(A))


def DeterminingTheOrder(Value):
    if Value == 2:
        DeterminantOfOrder2()
    elif Value == 3:
        DeterminantOfOrder3()
    else:
        print("Вы ввели не то значение!")


while cycle:
    check = int(input("Введите порядк предела: "))
    DeterminingTheOrder(check)

    check2 = input("Если вы хотите ввести определитель, напишите \"Да\", а если не хотите, то \"Нет\": ")

    cycle2 = True
    while cycle2:
        if check2 == 'Да':
            cycle2 = False
            cycle = True
        elif check2 == 'Нет':
            cycle2 = False
            cycle = False
        else:
            print("Вы ввели не то значение!")
            cycle2 = False



