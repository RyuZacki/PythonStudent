
DotaHeroes = ["Абадон", "Алхимик", "Акс", "Бистмастер", "Брюмастер", "Бристалбэк", "Кентавр", "Цк", "Слок", "Дум",
              "Дк", "Земеля", "Шейкер", "Титан", "Хускар", "Висп", "Кунка", "Лега", "Гуля", "Люкан",
              "Магнус", "Марс", "Баланар", "Омник", "Феникс", "Пудгер", "Сэнд Кинг", "Слардар", "Снэпфаер", "Бара",
              "Свен", "Тайд", "Тимбер", "Тини", "Трент", "Таск", "Андерлорд", "Андет", "Вк",
              "Антимаг","Арк Варден","Блудсикер","Бх","Бруда","Склинкз","Дровка","Эмбер","Войд","Гиро",
              "Худвинк","Джага","Лон Друид","Луна","Медуза","Мипо","Мирана","Мк","Морф","Нага",
              "Никс","Пангольер","Фантомка","Лансер","Разор","Рики","Сф","Сларк","Снайпер","Спектра",
              "Темпларка","Тб","Троль","Урса","Венга","Веник","Вайпер","Вивер"
              "Апарат","Бэйн","Батрайдер","Чен","Цм","Дарк Сир","Дарк Вилоу","Дазл","Парафетка","Дизраптор",
              "Энча","Энигма","Грим","Инвок","Джакиро","Котл","Лешрак","Лич","Лина","Лион",
              "Фурион","Некр","Огр","Оркл","Од","Пак","Пугна","Квапа","Рубик","Шадоу Демон",
              "Раста","Сало","Петух","Шторм","Течис","Тинкер","Визаж","Войд Спирит","Варлок","Вр",
              "Виверна","Вд","Зевс"]

Dire = []
Radiant = []


def checkForHeroes(type, heroes):
    while True:
        HeroFind = False
        Heroes = input("Введите героя для {type}: ".format(type=type))
        for i in DotaHeroes:
            if i == Heroes:
                heroes.append(i)
                HeroFind = True
                break

        if HeroFind:
            print("{0} был добавлен!".format(Heroes))
        else:
            print("{0} не был найден!".format(Heroes))

        if len(heroes) == 5:
            print("Все герои {type} добавлены!".format(type=type))
            break

checkForHeroes("Dire", Dire)
checkForHeroes("Radiant", Radiant)

