# --- Работа с фото ---
import cv2
import numpy as np

img = cv2.imread('images/yra1.jpg')  # Прочтение фотографии
# Метод imshow принимает два параметра ('Название фото', 'Само фото')
# new_img = cv2.resize(img, (300, 500))  # Изменение размеров изображения
# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))  # Изменение размеров изображения  unnamed.png
img = cv2.resize(img, (1600, 900))
img = cv2.GaussianBlur(img, (5, 5), 0)  # Добавление размытия
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Изменение формата фотографии

# Узнаём углы фотографии (Контуры)
# Переводим в бинарный формат
img = cv2.Canny(img, 35, 35)  # Для большей точности понижаем значения

kernel = np.ones((3, 3), np.uint8)  # Создаём матрицу
img = cv2.dilate(img, kernel, iterations=1)  # Измение размера контуров

#img = cv2.erode(img, kernel, iterations=1)  # Изменение контуров

cv2.imshow('Result', img)  # Открытие фотографии
# cv2.imshow('Result', img[0:100, 0:150])  # Обрезание фотографии

print(img.shape)  # Узнаем размер картинки (Высота, ширина, кол.слоёв)

cv2.waitKey(0)  # Задержка (в милисекундах 1000 = 1 сек)
