#-----------------------------------------------------------------------------------------------------------------------
#                                                  ООП Python
#-----------------------------------------------------------------------------------------------------------------------

"""Создание класса"""
class Car:  # <-- Создание
    model = "BMW"
    engine = 1.6

a = Car()  # <-- Создание экземпляра класса (к переменной a присвоили класс Car())

#-----------------------------------------------------------------------------------------------------------------------

""" Атрибуты класса """
class Person:
    """ Созданные нами атрибуты класса """
    name = 'Ivan'
    age = 30

getattr(Person, 'name') # Обращение к атрибуту (Person.name)
Person.name = 'Misha'
Person.aa = 200 # Если присвоить значение к не сушествующему атрибуту, то питон добавит этот атрибут в класс
setattr(Person, 'aa', 250) # Изменение атрибута Person.aa = 250
Person.bb = 10
del Person.aa # Удаление атрибута aa
delattr(Person, 'bb') # Так же удаление

#-----------------------------------------------------------------------------------------------------------------------

""" Атрибуты экземпляра класса """
class Car2:
    model1 = "BMW"
    engine1 = 1.6

a1 = Car2()
a2 = Car2()

a1.seat = 4 # Создал атрибут для экземпляра класса
a1.model = 'Lada'

a2.size = 80
Car2.r = 100

#-----------------------------------------------------------------------------------------------------------------------

""" Функция как атрибут класса """
class Car3:
    model2 = "BMW"
    engine2 = 1.6

    @staticmethod
    def drive(): # Функция внутри класса
        print("Let's go")

Car3.drive() # Вызов функции через класс
getattr(Car3, 'drive')() # Вызов функции через класс

b6 = Car3()
b6.drive()

#-----------------------------------------------------------------------------------------------------------------------

""" Методы класса, параметр self """
class Point:
    def __init__(self, x, y): # <-- Метод __init__ (Конструктор)
        print("Создание экземпляра класса Point")
        self.x = x
        self.y = y

    def __del__(self): # <-- Метод __del__ (Деструктор)
        print("Удаление экземпляра: " + self.__str__())

    """ Создание метода """
    def setCoords1(self): # <-- Метод
        print(self.__dict__)

    def setCoords2(self, x, y): # <-- Метод
        print(self.__dict__)
        self.a = x
        self.b = y

pt = Point(5, 10)
#pt.x = 5
#pt.y = 10
pt.setCoords1()
pt.setCoords2(7, 13)

#-----------------------------------------------------------------------------------------------------------------------

""" Инкапсуляция, геттеры и сеттеры """
class Point1:
    WIDTH = 5
    #__slots__ = ["__x", "__y"]  # шото там где мы можем указывать любые свойства экзмляров класса

    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y # __ режим доступа private

    """ isinstance это функция которая служит проверкой x на тип int, либо какой другой  """
    def __chekValue(x): # Приватный метод
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def setCorrds(self, x, y): # setCorrds это публичный метод (сеттер из-за тега set)

        if Point1.__chekValue(x) and Point.__chekValue(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами!")

    def getCoords(self): # getCoords это публичный метод (геттер из-за тега get)
        return self.__x, self.__y

    def __getattribute__(self, item): # Перегрузка метода
        if item == "_Point__x":
            return "Частная переменная"
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value): # Перегрузка метода
        if key == 'WIDTH':
            raise AttributeError # Вызывает исключение
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print("__getattr__: " + item)

    def __delattr__(self, item):
        print("__delattr__: " + item)


pt = Point1(1, 2)
print( pt.getCoords() )
#print(pt.__x) <-- к этому атрибуту нельзя обратиться
pt.setCorrds("10", 20) # <-- Теперь можно
print( pt.getCoords() )
print(pt._Point1__x) # Один из способов, как можно обратиться к приватному атрибуту

#-----------------------------------------------------------------------------------------------------------------------

""" Property """
class Point3:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    @property
    def coordX(self):  # __getCoordX

        return self.__x

    @coordX.setter
    def coordX(self, x):  # __setCoordX
        if Point3.__checkValue(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных")

    @coordX.deleter
    def coordX(self):  # __delCoordX
        print("Удаление свойства")
        del self.__x

    # coordX = property(__getCoordX, __setCoordX, __delCoordX)


pt = Point3(1, 2)
pt.coordX = 100  # Запись значения
x = pt.coordX  # Чтение значения
print(x)
# del pt.coordX

#-----------------------------------------------------------------------------------------------------------------------

""" Дескрипторы """
class CoordValue:
    # def __init__(self, name):
    #     self.__name = name

    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    # def __delete__(self, obj):
    #     del self.__value


class Point4:
    coordX = CoordValue() # coordX = CoordValue("CoordX")
    coordY = CoordValue() # coordY = CoordValue("CoordY")

    def __init__(self, x = 0, y = 0):
        self.coordX = x
        self.coordY = y


pt = Point4(1, 2)
pt2 = Point4(10, 20)
pt.coordX = 5
print(pt.coordX, pt.coordY)
print(pt2.coordX, pt2.coordY)

#-----------------------------------------------------------------------------------------------------------------------

""" Статические методы и свойства класса """
class Point5:
    __count = 0 # <-- Статическое свойство
    __instance = None

    """ Метод new выполняется перед темкак создать экземпляр класса Point5 """
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Point5, cls).__new__(cls)
        else:
            print("Экземпляр класса Point5 уже создан!")

    def __init__(self, x = 0, y = 0):
        Point5.__count += 1
        """ Локальное свойство """
        self.coordX = x
        self.coordY = y

    """ Статический метод """
    @staticmethod
    def getCount():
        return Point5.__count


pt = Point5()
pt2 = Point5()
pt3 = Point5()
# print(pt.getCount())

# Point5.count = 10
# pt.count = 0  <-- Локальное свойство
# print(pt.count, pt2.count, pt3.count)

#-----------------------------------------------------------------------------------------------------------------------


