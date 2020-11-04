import numpy as np
import matplotlib.pyplot as plt

N = 5 # образы для 1 и 2 класса

''' Моделируем класса '''
x1 = np.random.random(N) # моделируем случайные велечины по одной оси x1
x2 = x1 + [np.random.randint(10)/10 for i in range(N)] # x2 будет моделироваться как x1 плюс случайное отклонение
''' Таким образов точки х1 и х2 будут лежать выше нашей прямой  '''
C1 = [x1, x2] # формируем двумерный списк состоящий из набора этих точек

''' Делаем тоже самое, что и с первыми точками  '''
x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10)/10 for i in range(N)] - 0.1 # - 0.1 нужно чтобы точка х2 была ниже прямой
C2 = [x1, x2]

f = [0, 1] # Формеруем прямую под 45 крадусов

w = np.array([-0.3, 0.3]) # Задайом веса для нашей НС
for i in range(N):
    ''' Перебераем все образы, как раз для класса C2 '''
    x = np.array([C2[0][i], C2[1][i]])
    y = np.dot(w, x) # Вычесляем входное значение
    if y >= 0:
        print("Класс C1")
    else:
        print("Класс C2")

plt.scatter(C1[0][:], C1[1][:], s = 10, c='red')
plt.scatter(C2[0][:], C2[1][:], s = 10, c='blue')
plt.plot(f)
plt.grid(True)
plt.show()
