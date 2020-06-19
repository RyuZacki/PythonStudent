import math
# Калькуль 4.0
while True:
    print('Выберите что хотите посчитать')
    p = input('Дискреминант(Des), производную(Pro), фактариал(Fak) или калькулятор(Kal): ')

    if p == 'Des':

        a = int(input('Введите значение a: '))
        b = int(input('Введите значение b: '))
        c = int(input('Введите значение c: '))


        if a > 0 and a != 0 :
            if b > 0 and b != 0:
                if c > 0 and c != 0 :
                    print('{0}x^2+{1}x+{2}'.format(a, b, c))
                else:
                    print('{0}x^2+{1}x{2}'.format(a, b, c))
            else:
                 if c > 0 and c != 0 :
                     print('{0}x^2{1}x+{2}'.format(a, b, c))
                 else:
                     print('{0}x^2{1}x{2}'.format(a, b, c))
        else:
            if b > 0 and b != 0:
                if c > 0 and c != 0 :
                    print('{0}x^2+{1}x+{2}'.format(a, b, c))
                else:
                    print('{0}x^2+{1}x{2}'.format(a, b, c))
            else:
                 if c > 0 and c != 0 :
                     print('{0}x^2{1}x+{2}'.format(a, b, c))
                 else:
                     print('{0}x^2{1}x{2}'.format(a, b, c))



        D = b**2 - 4 * a * c
        if D > 0:
            print('Дискреминант равен корень из {}'.format(D))

            x1 = (-b + math.sqrt(D)) / 2 * a

            x2 = (-b - math.sqrt(D)) / 2 * a

            print('Уравнение имеет два корня x1 = {0}, х2 = {1}'.format(x1,x2))

        elif D == 0:
            print('Дискреминант равен {}'.format(D))

            x = (-b) / 2 * a

            print('Уравнение имеет один корень х = {}'.format(x))
        else:
            print('Дискреминант равен корень из {}'.format(D))
            print('Уравнение не имеет корней')

        End = input('Желаете продолждить ?(n/y): ')
        if End == 'y':
            continue
        elif End == 'n':
            break

    elif p == 'Pro':

        a1 = int(input('Введите число: '))
        b1 = int(input('Введите степень числа: '))

        print('{0}x^{1}'.format(a1,b1))

        x1 = a1 * b1
        x2 = b1 - 1

        print('Производна равна {0}x^{1}'.format(x1,x2))

        End = input('Желаете продолждить ?(n/y): ')
        if End == 'y':
            continue
        elif End == 'n':
            break

    elif p == 'Fak':

        n = int(input('Введите число: '))

        factorial = 1

        for i in range(2, n + 1):
            factorial *= i

        print('Факториал числа {0} равен {1}'.format(n,factorial))

        End = input('Желаете продолждить ?(n/y): ')
        if End == 'y':
            continue
        elif End == 'n':
            break

    elif p == 'Kal':

        what = input("Что делаем? (+,-,*,/,**,%,!,Cos,Sin,sqrt): ")
        a = float(input("Введите значение a: "))
        b = float(input("Введите значение b: "))
        i = 1

        if what == "+":
            c = a + b
            print("Результат: " + str(c))
        elif what == "-":
            c = a - b
            print("Результат: " + str(c))
        elif what == "*":
            c = a * b
            print("Результат: " + str(c))
        elif what == "/":
            c = a / b
            print("Результат: " + str(c))
        elif what == "**":
            c = a**b
            print("Результат: " + str(c))
        elif what == "%":
            c = a % b
            print("Результат: " + str(c))
        elif what == "!":
            while a > 1:
                i *= a
                a -= 1
        elif what == "Cos":
            print(math.cos(a))
        elif what == "Sin":
            print(math.sin(a))
        elif what == "sqrt":
            print(math.sqrt(a))
        else:
            print("Вы выбрали не правильное действие!")
        print(i)

        End = input('Желаете продолжить? Y/N ' )
        if End == 'Y':
            continue
        elif End == 'N':
            break
