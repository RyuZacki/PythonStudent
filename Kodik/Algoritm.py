import math
#------------------------
# 1.Сортировка пузырьком
#------------------------

#*---1---
nums = [2,5,1,8,7,3,4,6,9]

print(nums)

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)

#*---2---
nums = [2,5,1,8,7,3,4,6,9]

print(nums)
swaps = True
while swaps:
    swaps = False

    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            swaps = True
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)

#------------------------
# 2.Факториал числа
#------------------------

#*---1---
number = 5

def factorial(n):
    if n == 0:
        return 1

    f = 1
    i = 0

    while i < n:
        i += 1
        f = f * i

    return f

print('Факториал числа {n} равен {f}'. format(n = number, f = factorial(number)))

#*---2---
number = 5

def factorial(n):
    if n == 0:
        return 1

    return factorial(n - 1) * n

print('Факториал числа {n} равен {f}'. format(n = number, f = factorial(number)))

#------------------------
# 3.Числа Фибоначчи
#------------------------

#*---1---
f1 = f2 = 1
n = 10

print(f1, end=' ')
print(f2, end=' ')

for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')

#*---2---
def fib(n):
    golden_ration = (1 + math.sqrt(5)) / 2
    val = (golden_ration**n -  (1 - golden_ration)**n) / math.sqrt(5)
    return int(round(val))

print(fib(10))

#*---3---
def fib():
    f1, f2 = 0, 1

    while True:
        yield f1
        f1, f2 = f2, f1 +f2

for i, f in zip(range(10 + 1), fib()):
    print("{i:3}: {f:3}".format(i = i, f = f))

#-------------------------
# 4.Расстояние Левенштейна
#-------------------------

#*---1---
def dist(a, b):
    def rec(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        elif a[i-1] == b[j-1]:
            return rec(i-1, j-1)
        else:
            return 1 + min(
                rec(i, j-1),
                rec(i-1, j),
                rec(i-1, j-1),
            )

    return rec(len(a), len(b))

str1 = "Привет"
str2 = "Првет"

lev = dist(str1, str2)
bigger = max([len(str1), len(str2)])
pct = ((bigger - lev) / bigger) * 100

print(
    "Строка #1 : {str1}\nСтрока #2 : {str2}"
    "\n===\nСхожесть : {pct}%".format(str1=str1,str2=str2,pct=pct)
)

#-------------------------
# 5.Односвязный списк
#-------------------------

#*---1---
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.head != None:
            c = self.head
            out = "LinkedList [" + str(c.value)

            while c.next != None:
                c = c.next
                out += ", " + str(c.value)

            out += "]"
            return out
        else:
            return "LinkedList []"

    def add(self, n):
        self.length += 1

        if self.head == None:
            self.head = self.tail = Node(n, None)
        else:
            self.tail.next = self.tail = Node(n, None)

    def reverse(self):
        pNode = None
        cNode = self.head
        nNode = cNode.next

        self.tail = None


L = LinkedList()

L.add(1)
L.add(2)
L.add(3)

print(L)



