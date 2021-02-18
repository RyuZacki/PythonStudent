from datetime import datetime

sqs = 0,1,4,9,16,25,36,49,64,81
print(sqs[7:5:-1])

sqs = 0,1,4,9,16,25,36,49,64,81
print( sqs[6:8:1])

#-----------------------------------------------------------------------------------------------------------------------

human = {
    "Тоха" : '+758573123',
    "Костик" : '+758213645',
    "Юрец" : '+758927564' }

print(human["Тоха"])

h = 'Lox'
print('{0:*^17}'.format( h ))

rtr = [1,3,5,6,1,3,123,42,33,65,7,234,44,56,71]
q = int(input('Введите число: '))
print(rtr[q])
f = 1
g = 1
print('Привет %s как дела %d' %(f, g) )

x = input('Введите имя: ')

if x in human:
    print('Номер {0} : {1}'.format (x, human[x]))
else:
    print('Вы ввели не то значение!')

#-----------------------------------------------------------------------------------------------------------------------

Name = input('Введите имя: ')

if Name.lower().startswith('а'):
    print('Привет, ' + str(Name))
elif Name.lower().startswith('ю'):
    print('Ну ты и дурак ' + str(Name))
else:
    print('Иди гуляй!')

#-----------------------------------------------------------------------------------------------------------------------

number = range(2, 17)[::2]

for i in number:
        print(i)

#-----------------------------------------------------------------------------------------------------------------------

input_str = input('Введи имя: ')
input_x = input('Знак: ')

if len(input_str) % 2 != 0:
    print(('{x:' + str(input_x) + '^16}').format(x=input_str))
else:
    print(('{x:' + str(input_x) + '^17}').format(x=input_str))

#-----------------------------------------------------------------------------------------------------------------------

fib1 = 1
fib2 = 1

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)

list = [1]

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2   # 8
    fib1 = fib2             # 3
    fib2 = fib_sum          # 5
    i = i + 1
    print(fib2)
    list.append(fib2)

print(list)
print(sum(list))
print('!!!!!' + str(fib2) + '!!!!!')

#-----------------------------------------------------------------------------------------------------------------------

name = input()
A = 'Yes' if name != 'Test' else 'No'
print(A)

#-----------------------------------------------------------------------------------------------------------------------

for j in 'hello world':
    if j == 'a':
        break
    print(j * 3, end = '')
else:
    print('Какаха')

#-----------------------------------------------------------------------------------------------------------------------

r = {i ** 2 for i in range(10)}
b = frozenset() #frozenset - множество которое нельзя изменить
s = set()   #set() - множество, s = {"23" : 23} - словарь, s = {"23", 23} - множество
print(type(s))
print(s)

a = tuple('hello world')
print(a)
d = dict(short='dict', longer='dictionary') # d = dict ([(23, 34), (56, 87)])
print(d)
y = dict.fromkeys(['a', 'b', 'c'], 1)
c = {z : z ** 2 for z in range(7)}

l = []
lis = [1, 56, 'x', 34, 2.34, ['s', 't', 'r', 'o', 'k', 'a']]
print(lis)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)
l.append(23) #Добавить значение
l.append(34)
b = [24, 67]
l.extend(b) #Добавить один список в другой
l.insert(1, 56) #Добавить значение по индексу
l.remove(34) #Удалить значение
l.pop(0) #Удалить значение по индексу
print(l.index(56)) #Узнать индекс значения
l.count(34) #Узнать сколько однатипных значений в списке
l.sort() #Рассортировка списка
l.reverse() #Перевернуть списк
l.clear() #Очистить списк

print(l)

#-----------------------------------------------------------------------------------------------------------------------

add1 = lambda x1, y1: x1 * y1 #print((lambda x1, y1: x1 * y1)(1, 5))
print(add1(1, 5))

def f1():
    try:
        a = int(input('Введите число: '))
        return a
    except ValueError:
        print("Вы ввели не то значение!")
        return None

def func(x): #Параметром для функции может быть (кортеж *x или словарь **x)
    def add(a):
        return x + a
    return add

test = func(100)
print = (test(200)) #print = 300

#-----------------------------------------------------------------------------------------------------------------------

'''

    __ООП__
1. Инкапсуляция
2. Наследование
3. Полиморфизм

'''

class Person:  # <-- Создание класса
    name = 'Ivan'
    age = 10

    def __init__(self, name, age): # <-- Конструктор
        self.name = name
        self.age = age

    def set(self, name, age): # <-- Метод
        self.name = name
        self.age = age


class student(Person):
    course = 1

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def set_course(self, name, age, course):
        super().set(name, age)
        self.course = course


igor = student('Igor', 19, 2)
# igor.set('Igor', 19)
print(igor.course)

vlad = Person('Влад', 25)  # Объект класса Person
# vlad.set('Влад', 25)
print(vlad.name + " " + str(vlad.age))

ivan = Person('Иван', 56)
# ivan.set('Иван', 56)
print(ivan.name + " " + str(ivan.age))

ivan = Person('Иван', 56)
#ivan.set('Иван', 56)
print(ivan.name + " " + str(ivan.age))
print(ivan.suka())

#1
class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):  # Функция __init__ отвечает за базовый функционал
        """Инициализируем атрибуты имя и возраст"""
        self.name = name
        self.age = age
        print("Собака создана")
        
    def sit(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + " сел")  #  title() - Выводит надпись с большой буквы!

    def jump(self):
        """Собака будет прыгать по команде"""
        print(self.name.title() + " прыгнул")

my_dog = Dog('Topik', 4)
my_dog2 = Dog('Nick', 7)

print(my_dog.age)
print(my_dog.name)

my_dog.jump()
my_dog2.sit()

#2
class Car():
    """Класс по созданию автомобиля"""

    def __init__(self, make, model, year):
        """Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def description_name(self):
        """Возвращаем описание автомобиля"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_odometer(self):
        """Выводим пробег авто"""
        print("Пробег этого авто " + str(self.odometer_reading) + " км")

    def update_odometer(self, km):
        """Устанавливаем значеиние на одометре"""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("Не стоит с этим баловаться")

    def increment_odometer(self, km):
        """Увеличиваем показания одометра на заданную велечину"""
        self.odometer_reading += km


class Battery():
    """Простая модель аккумулятора для электромобиля"""

    def __init__(self, battery=100):
        self.battery = battery

    def description_battery(self):
        """Выводит информацию о мощности батареи"""
        print("Этот автомобиль имеет батарею мощностью " + str(self.battery) + "киловат")


class ElectricCar(Car):
    """Аспекты для электромобтля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов класса родителя"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def description_name(self):
        """Переопределение родительского метода"""
        desc = str(self.year) + ' ' + self.model
        return desc.title()


tesla = ElectricCar('tesla', 's', 2017)
tesla.battery.description_battery()

# tesla = ElectricCar('tesla', 's', 2017)
# print = (tesla.description_name())
# tesla.description_battery()

# my_car = Car('audi', 'a4', 2017)
# #my_car.odometer_reading = 30
# my_car.update_odometer(24)
# my_car.increment_odometer(150)
#
# #print(my_car.description_name())
# my_car.read_odometer()

#-----------------------------------------------------------------------------------------------------------------------
'''Для игры!'''

#       if keys[pygame.K_UP] and y > 5:
#           y -= speed
#       if keys[pygame.K_DOWN] and y < 500 - height - 5:
#            y += speed

#-----------------------------------------------------------------------------------------------------------------------

a = ['H','e','l','l','o',' ','W','o','r','l','d']
b = len(a)
print(b)
print(a)

char_list = []
string = 'май'
for c in string:
    char_list.append(c)
print(char_list)

print(a[0])
# Rainbow[0] = 'красный'
print('Выведем радугу')
for i in range(len(a)):
    print(a[i])

#-----------------------------------------------------------------------------------------------------------------------

#ДЕКОРАТОР1.0
def decor(func):
    def wrap():
        print('============')
        func()
        print('============')
    return wrap

@decor
def print_text():
    print('Hello world!')

print_text()

# ----------------------------------------------------------------------------------------------------------------------

#РЕКУРСИЯ
def factarial(x):
    if x == 1:
        return 1
    else:
        return x * factarial(x - 1)

print(factarial(5))

#============

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))

#============

# ----------------------------------------------------------------------------------------------------------------------

#МНОЖЕСТВА
num_set = {1, 2, 3, 4, 5}
word_set = set(['spam', 'eggs', 'sausage'])

print(3 in num_set)
print('spawn' not in word_set)

#============

nums = {1, 2, 3, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

#============

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
 #Операторы
print(first | second) # <-- Оператор объединения (|) объединяет два множества в одно, содержащее все элементы двух множеств
print(first & second) # <-- Оператор пересечения (&) возвращает только элементы, находящиеся в обоих множествах
print(first - second) # <-- Оператор разности (-) возвращает элементы только с первого множества
print(second - first)
print(first ^ second) # <-- Оператор симмерической разности (^) возвращает все элементы с обоих множест, кроме принадлежащих
                      # одновременно обоим

#============

# ----------------------------------------------------------------------------------------------------------------------

a = input('Введите число: ')

b = type(a)
if b == str:
    print('Зелебоба')
else:
    print('Кукусик')

# ----------------------------------------------------------------------------------------------------------------------

#Списки
my_list = []
my_list1 = list()
#----------------
combo_list = [1]
one_list = [4, 5]
a = combo_list.extend(one_list)

print(a)  # [1, 4, 5]
#----------------
alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()

print(alpha_list)  # [2, 23, 34, 67, 88, 100]


#Кортежи
my_tuple = (1, 2, 3, 4, 5)
a = my_tuple[0:3]
print(a)  # (1, 2, 3)

another_tuple = tuple()
abc = tuple([1, 2, 3])


#Словари
my_dict = {}
another_dict = dict()

my_other_dict = {"one": 1, "two": 2, "three": 3}
print(my_other_dict)  # {'three': 3, 'two': 2, 'one': 1}
#----------------
my_other_dict = {"one": 1, "two": 2, "three": 3}

print(my_other_dict["one"])  # 1

my_dict1 = {"name": "Mike", "address": "123 Happy Way"}
print(my_dict1["name"])  # 'Mike'

# ----------------------------------------------------------------------------------------------------------------------

# Что означает *args и **kwargs

# def do_smth(*args, **kwargs):
#     pass

def gen(): # <-- Генератор
    for i in range(10):
        yield i

def add(*args, **kwargs): # Одна * это упаковка в кортеж, две * это упаковка в словарь
    print(args)
    #print(sum(args))
    print(kwargs)

l = [1,2,3]
l1 = {'street': 'leninia', 'house': 12}
add(*l, **l1) # <-- Можно записать вот так
add(1,2,3, street = 'leninia', house = 12 ) # А можно так
#add(*gen())

# ----------------------------------------------------------------------------------------------------------------------

# if __name__ == '__main__':

a ='123'

def add1():
    pass

print(globals()) # <-- Какой то скрипт который возвращает словарь

print("Imported from: ", __name__) # Тоже шото то за скрипт
# __name__ то служебная встроенная переменная, которая хранит имя модуля

def main():
    pass

if __name__ == '__main__': # <-- Если модуль был запущен как самостоятельный то выполняется следующее
    main()

# ----------------------------------------------------------------------------------------------------------------------

# Генераторы списков

jack = {
    'name': 'jack',
    'car': 'bmw'
}

john = {
    'name': 'john',
    'car': 'audi'
}

users = [jack, john] # <-- Списк словарей

# cars = [person['car'] for person in users] # <-- Генератор списков
# print(cars)

cars = []
for person in users:
    cars.append(person['car'])

# print(cars)

new_cars = [person.get('car', '') for person in users]
print(new_cars)

# ----------------------------------------------------------------------------------------------------------------------

# Фильтрация

names = ['jack', 'john', 'oleg', 'ula']

new_names = [n for n in names if n.startswith('j')]

print(new_names)

new_names = []
for n in names:
    if n.startswith('j'):
        new_names.append(n)

print(new_names)

# ----------------------------------------------------------------------------------------------------------------------

#Декораторы2.0


def timeit(arg): # <-- Тут я получаю функцию, как объект
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs) # <-- Тут я вызвал функцию, которую получиь на входе
            print(datetime.now() - start)
            return result
        return wrapper
    return outer


@timeit('name')
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit('name')
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l

l1 = timeit('name')(one)(10)

# l1 = timeit(one)(10) # => wrapper(10) => one(10)
# print(type(l1), l1.__name__)

# l1 = one
# a = l1(10)
# print(a)

# l1 = one(10000)
# l2 = two(10000)
#
# #print(l1)
# #print(l2)

# ----------------------------------------------------------------------------------------------------------------------

def test(x, y, z):
    print(x, y, z)

l = [1,2,3]
d = {'x': 1, 'y': 2, 'z': 3}

test(*l)
test(**d)

# ------------

d = {'sum': lambda x,y: x + y,
     'sub': lambda x,y: x - y}

print(d['sum'](1, 2))
print(d['sub'](1, 2))

# ----------------------------------------------------------------------------------------------------------------------

#Исключения
def calc(m):
    # 1000 : 10 = m : x
    try:
        m = int(m)
    # except Exception:
    # except Exception as e:
    except ValueError as e:
        print(e)
        # print('Что то пошло не так ')
        m = 0
    except TypeError:
        pass
    except FileNotFoundError:
        pass
    else: # <-- блок else выполняется если в блоке try не произошло исключения
        return 10 * m / 1000
    finally: # <-- Этот блок отвечает за тот кусок кода который выполняется в любом случае
        print('Hi')


print(calc('1gfg'))

# ----------------------------------------------------------------------------------------------------------------------

#Генератор
def gen_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1

g = gen_countdown(4)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for i in gen_countdown(4):
    print(i)

# ----------------------------------------------------------------------------------------------------------------------

# Функция map()
def upper(string):
    return string.upper()


l = ['one', 'two', 'three']

new_list = list(map(upper, l))
print(new_list)

new_l = list(map(lambda string: string.upper(), l))
print(new_l)

nl = [string.upper() for string in l]
print(nl)


def map1(func, iterable): # <-- Эта фунуция эквевалентна функции map()
    for i in iterable:
        yield func(i)

# ----------------------------------------------------------------------------------------------------------------------

# Функция filter()

def has_o(string):
    return 'o' in string.lower()


l = ['One', 'two', 'three', '23Fkjsf']

nl = list(filter(has_o, l))
print(nl)

newl = list(filter(lambda string: 'o' in string.lower(), l))
print(newl)

nl2 = [string for string in l if has_o(string)]
print(nl2)

# ----------------------------------------------------------------------------------------------------------------------

# Else у циклов For и While

for i in range(5):
    if i == 6:
        print(i)
        break
else:
    print('The end')

flag = False
for i in range(5):
    if i == 4:
        flag = True
        break

if flag:
    print('Six was found')

# ----------------------------------------------------------------------------------------------------------------------

# Генератор списка
a = [i**2 for i in range(1, 6)]
print(a)

# Выражения-генераторы

b = (i**2 for i in range(1, 6)) # Отличия от генератора списков только в скобках
print(b)
for i in b:
    print(i)

# print(next(b))
# print(next(b))
# print(next(b))

s = [1, 2, 3]
d = iter(s) # Делаем из списка итератор
next(d)

# ----------------------------------------------------------------------------------------------------------------------

# Функции all и any

a = ['hello', '', 'world']
b = [1, 2, 3]
print(all(a)) # Функция all должна принимать коллекцию(объект состоящий из нескольких объектов)
# all пробегается по всем элементам коллекции и преобразует их в тип bool
print(any(a)) # Принимает на вход коллекцию и она будет равна истене если хотя бы один элемент из коллекции будет являтся не пустым

print(all(a))
print(any(b))

x = 100

condition_1 = x % 2 == 0
condition_2 = x > 50
condition_3 = x < 1000

print(all([condition_1,condition_2,condition_3]))
print(any([condition_1,condition_2,condition_3]))

# ----------------------------------------------------------------------------------------------------------------------

# Замыкания
def main_func(value): # <-- Главная функция
    name = value
    def inner_func(): # <-- Вложенная функция
        print("Hello my friend", name)

    return inner_func


a = main_func('Misha')
a()


def adder(value):
    def inner(a):
        return value + a

    return inner

a2 = adder(2) # <-- value = 2
print(a2(5)) # <-- a = 5, после чего мы value + a и получаем 7


def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count

    return inner


q = counter()
print(q()) # <-- выведит 1
print(q()) # <-- выведит 2
print(q()) # <-- выведит 3

# ----------------------------------------------------------------------------------------------------------------------

# Декораторы 3.0
def decorator(func):
    def inner(*args, **kwargs):
        print("start decorator...")
        func(*args, **kwargs)
        print("finish decorator...")
    return inner


def say(name, surname, age):
    print("Hello, ", name, surname, age)


say = decorator(say)
say("Vasya", "Ivanov", 30)

print(" ")


def header(func):
    def inner(*args, **kwargs):
        print("<h1>")
        func(*args, **kwargs)
        print("</h1>")
    return inner


def table(func):
    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")
    return inner


def say(name, surname, age):
    print("Hello, ", name, surname, age)


say = table(header(say))
say("Vasya", "Ivanov", 30)

# ----------------------------------------------------------------------------------------------------------------------

#Параметры print
print("Hello world!")
print("Hello world!")
print("I\'m fine!")

a = 10
b = 10.23
c = "Hello"

print(a)
print(b)
print(c)

print("Value of a = ", a)
print("Value of b = ", b)
print("Value of c = ", c)


print("Hello friends how are you?", end = ' ')
print("I am fine!", end ='#')
print() # prints new line

print("ABC", end='')
print("PQR", end='\n') # ends with a new line

print("This is line 1.", end='[END]\n')
print("This is line 2.", end='[END]\n')
print("This is line 3.", end='[END]\n')

# ----------------------------------------------------------------------------------------------------------------------

#Срезы

a = [1, 3, 8, 7]
var = a[:]  #[1, 3, 8, 7]
var1 = a[1:] #[3, 8, 7]
var2 = a[:3] #[1, 3, 8]
var3 = a[::2] #[1, 8]

a = [1, 3, 8, 7]
var4 = a[::-1] #[7, 8, 3, 1]
var5 = a[:-2] #[1, 3]
var6 = a[-2::-1] #[8, 3, 1]
var7 = a[1:4:-1] #[]

a = [1, 3, 8, 7]
var8 = a[10:20] #[]

a = [1, 3, 8, 7]
a[1:3] = [0, 0, 0]
del a[:-3]

# ----------------------------------------------------------------------------------------------------------------------