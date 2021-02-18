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
