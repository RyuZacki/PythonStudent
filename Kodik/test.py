import math
# Калькуль 4.0
while True:
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
