
from full_name import full_name

print("Для остановки теста введите символ 'Q'")
while True:
    first = input("\nВведите ваше имя: ")
    if first == 'Q':
        break
    last = input("\nВведите вашу фамилию: ")
    if last == 'Q':
        break

    format_name = full_name(first, last)
    print("\tФорматирование имени: " + format_name)

