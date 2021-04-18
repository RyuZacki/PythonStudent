#Глава 1
#-------------------------
# 1.Бинарный поиск
#-------------------------

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

#Глава 2
#-------------------------
# 2.Сортировка выбором
#-------------------------

def  findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))

#Глава 3
#-------------------------
# 3.Рекурсия
#-------------------------

#.Перебор коробок через цикл while
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")

#.Перебор коробок через рекурсию
def look_for_key2(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key!")

#.Базовый и рекурсивный случай
def countdown(i):
    print(i)
    if i <= 1: # <-- Базовый случай
        return
    else:
        countdown(i - 1) # <-- Рекурсивный случай

#.Стек вызовов
def greet(name):
    print("Hello, " + name + " ?")
    greet2(name)
    print("Getting ready to say bye...")
    bye()

def greet2(name): # Когда вызывается функция greet2, функция greet находится в незавершонном остановленном состаянии
    print("how are you, " + name +" ?")
def bye(): # Перед функцией bye, функция greet2 полность завершается и освобождает ячейку памяти
    print("ok bye!")

#.Фактариал
def fact(x):
    if x == 1: # <-- Базовый случай
        return 1
    else:
        return x * fact(x - 1) # <-- Рекурсивный случай

#.4.1 - Сумма значений
def sum(list):
    if list == []: # <-- Базовый случай
        return 0
    return list[0] + sum(list[1:]) # <-- Рекурсивный случай

print(sum([2,4,6]))

#.4.2 - Подсчёт элементов
def count(list):
    if list == []: # <-- Базовый случай
        return 0
    return 1 + sum(list[1:]) # <-- Рекурсивный случай

print(count([2,4,6]))

#.4.3 - Максимальное значение
def max(list):
    if len(list) == 2: # <-- Базовый случай
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub-max else sub_max # <-- Рекурсивный случай

#Глава 4
#.Быстрая сортировка
def quicksort(array):
    if len(array) < 2:
        return  array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

#Глава 5
#Хеш-таблицы(Словари)
book = dict() # <-- Создание пустой хеш-таблицы(словаря)
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)
print(book["avocado"])

voted = {}
value = voted.get("tom") # <-- Функция get проверяет наличие имени том в хещ-таблице
#Если ключ tom есть в хеш-таблице, то функция get вернёт значение, а если ключа нету, то вернёт None

#.Реализация get()
voted1 = {}
def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

check_voter("tom")
print(voted1)
check_voter("mike")
print(voted1)
check_voter("mike")
print(voted1)

#.Кэширование
cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url] # <-- Возвращает кэшированные данные
    else:
        data = get_data_fron_server(url)
        cache[url] = data # <-- Данные сначала сохраняются в кэше
        return data

#Глава 6
#Поиск в ширину

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")