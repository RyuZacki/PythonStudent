import numpy as np

''' Вспомогательная функция (Функция активации) '''
def act(x):
    return 0 if x < 0.5 else 1

''' Функция которая пропускает через НС входные сигналы  '''
def go(house, rock, attr):
    x = np.array([house, rock, attr]) # Формеруем вектор входного сигнала
    w11 = [0.3, 0.3, 0] # Веса для 1 нейрона скрытого слоя
    w12 = [0.4, -0.5, 1] # Веса для 2 нейрона скрытого слоя
    weight1 = np.array([w11, w12]) # Матрица 2х3 (В которой мы объединяем веса)
    weight2 = np.array([-1, 1]) # Вектор 1х2 для вфходного нейрона

    sum_hidden = np.dot(weight1, x) # Вычисляем сумму на входах нейронов скрытого слоя
    print("Значения сумм на нейронах скрытого слоя: "+str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print("Значение на выходах нейронов скрытого слоя: "+str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print("Выходное значение НС: "+str(y))

    return y


house = 1
rock = 0
attr = 1

res = go(house, rock, attr)
if res == 1:
    print("Все норм")
else:
    print("Лох")
