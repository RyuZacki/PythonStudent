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
    pritn(j * 3, end = '')
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

class Person:  # <-- Создание класса
    name = 'Ivan'
    age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self, name, age):
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

#-----------------------------------------------------------------------------------------------------------------------
'''Для игры!'''

#       if keys[pygame.K_UP] and y > 5:
#           y -= speed
#       if keys[pygame.K_DOWN] and y < 500 - height - 5:
#            y += speed

#-----------------------------------------------------------------------------------------------------------------------

