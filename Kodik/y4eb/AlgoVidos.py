# ----- Алгоритмы и структуры данных -----

import graphics as gr

# Линейный поиск
def array_search(A:list, N:int, x:int):
    """ Осуществлят поиск числа x в массиве A
        от 0 до N-1 индекса в включительно
        Возвращает индекс элемента x в массиве A
        или -1, если такого нет """

    for k in range(N):
        if A[k] == k:
            return k
        return -1

def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test 1 - ok")
    else:
        print("#test 1 - fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test 2 - ok")
    else:
        print("#test 2 - fail")

    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("#test 3 - ok")
    else:
        print("#test 3 - fail")

# Обращение массива
def invert_array(A:list, N:int):
    """ Обращение массива(задом наперёд)
        в рамках индексов от 0 до N-1 """

    for k in range(N // 2):
        A[K], A[N - 1 - k] = A[N - 1 -K], A[k]


def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    invert_array(A1, 5)
    if A1 == [5, 4, 3, 2, 1]:
        print("#test 1 - ok")
    else:
        print("test 1 - fail")

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    invert_array(A2, 8)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test 2 - ok")
    else:
        print("test 2 - fail")

# Циклические сдвиги

# влево
tmp = A[0]
for k in range(N - 1):
    A[k] = A[k + 1]
A[N-1] = tmp

# вправо
tmp = A[N - 1]
for j in range(N - 2, -1, -1):
    A[j + 1] = A[j]
A[0] = tmp

# Тернарный оператор
p = 1 # Тут должен быть цикл
print(p, '-', "простое" if A[p] else "составное")

# Сортировка
def insert_sort(A):
    """ сортировка списка A вставками """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def choise_sort(A):
    """ сортировка списка A выбором """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """ сортировка списка A методом пузырьком """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


def test_sort(sort_algorithm):
    pritn("Тестирем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")


# if __name__ == "__main__":
#     test_ort(insert_sort)
#     test_ort(choise_sort)
#     test_ort(bubble_sort)

# Сортировка подсчётом
N = None
F = [0]*10
for i in range(N):
    x = int(input())
    F[x] += 1

# Рекурсия
window = gr.GraphWin("Russian game", 600, 600)
alpha = 0.2

def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
    B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
    C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
    D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)
    fractal_rectangle(A1, B1, C1, D1, deep-1)


fractal_rectangle((100, 100),(500, 100), (500, 500), (100, 500))

# Фактариал
def f(n:int):
    assert n >= 0, "Фактариал отрицательного не определён"
    if n == 0:
        return 1
    return f(n-1) * n


# Алгоритм Евклида
# -1-
def gcd1(a, b):
    if a == b:
        return
    elif a > b:
        return  gcd(a-b, b)
    else: # a < b
        return gcd(a, b-a)

# -2-
def gcd2(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# -3-
def gcd3(a, b):
    return a if b == 0 else gcd(b, a%b)

# Быстрое возведение в степень
def pow(a:float, n:int):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n-1) * a
    else:
        return pow(a**2, n//2)

# Ханойские башни
