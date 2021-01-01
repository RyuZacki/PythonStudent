import DotaHeroes

DireList = []
RadiantList = []

Dire = "Dire"
Radiant = "Radiant"


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


checkForHeroes(Dire, DireList)
checkForHeroes(Radiant, RadiantList)
