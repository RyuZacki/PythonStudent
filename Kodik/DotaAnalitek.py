import DotaHeroes

DireList = []
RadiantList = []

Dire = "Dire"
Radiant = "Radiant"

teamDire = {"Саппорт 5": None, "Саппорт 4": None, "Офлейнер": None, "Кери": None, "Мид": None,}
teamRadiant = {"Саппорт 5": None, "Саппорт 4": None, "Офлейнер": None, "Кери": None, "Мид": None,}

WinPercentage = 100

def lineDistributor(type, team):
    print("Распределите роли для команды {0}".format(type))
    Sup5 = input("Введите саппорта 5: ")
    team["Саппорт 5"] = Sup5
    Sup4 = input("Введите саппорта 4: ")
    team["Саппорт 4"] = Sup4
    Offlaneer = input("Введите офлейнера: ")
    team["Офлейнер"] = Offlaneer
    Keri = input("Введите кери: ")
    team["Кери"] = Keri
    Mid = input("Введите мидера: ")
    team["Мид"] = Mid


def wasPeek(Hero):
    peek = Hero in RadiantList or Hero in DireList

    if peek: print("{0} уже был пикнут!".format(Hero))

    return peek


def checkForHeroes(type, heroes):
    while True:
        HeroFind = False
        Hero = input("Введите героя для {type}: ".format(type=type))
        for i in DotaHeroes.DotaHeroes:
            if i == Hero and not wasPeek(Hero):
                heroes.append(i)
                HeroFind = True
                break

        if HeroFind:
            print("{0} был добавлен!".format(Hero))
        else:
            print("{0} не был добавлен!".format(Hero))

        if len(heroes) == 5:
            print("Все герои {type} добавлены!".format(type=type))
            break

while True:
    while True:
        if len(DireList) and len(RadiantList) == 5:
            break
        else:
            checkForHeroes(Dire, DireList)
            checkForHeroes(Radiant, RadiantList)

        print(" ====  Герои Dire  ==== ")
        print(DireList)
        print(" ====  Герии Radiant  ==== ")
        print(RadiantList)
        print(" ==== Расперделите роли ==== ")

        lineDistributor(Dire, teamDire)
        lineDistributor(Radiant, teamRadiant)

        print(" ====  Герои Dire с ролями  ==== ")
        print(teamDire)
        print(" ====  Герии Radiant с ролями  ==== ")
        print(teamRadiant)

    break
