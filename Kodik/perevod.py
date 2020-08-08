while True:
    text = input('Что делаем из 10 в 2 или из 2 в 10(10 - 2): ')
    binary_code = []
    if text == '10':
        a = int(input('Введите значение: '))

        b = 0
        while True:
            if a % 2 == 1:
                a = (a - 1) / 2
                binary_code.append(1)
            elif a % 2 == 0:
                a = a / 2
                binary_code.append(0)

            if a == 1:
                binary_code.append(1)
                break
            elif a == 0:
                binary_code.append(0)
                break

        binary_code.reverse()
        print(binary_code)
    elif text == '2':
        discharges = []
        x1 = 0

        n = input('Введите значение: ')
        num1 = []
        for i in n:
            x2 = int(i)
            num1.append(x2)

        x = len(num1)
        number = list(range(x))
        number.reverse()
        for i in num1:
            if i == 1:
                y = number[x1]
                num = 1 * 2**y
                x1 += 1
                discharges.append(num)
            else:
                x1 += 1

        sum_of_digits = sum(discharges)
        print(sum_of_digits)
    else:
        print('Вы ввели не то значение')

    text1 = input('Хотите попробывать ещё раз?(N/Y): ')
    if text1 == 'Y':
        continue
    else:
        break