import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')  # Создание матрицы

# RGB - стандарт
# BGR - формат в OpenCV
# photo[100:150, 200:280] = 119, 201, 105  # Окраска фото

# Рисуем квадрат
# В метод rectengle мы указываем само изображение, координаты прорисовки (2 и 3 значение), цвет и толщина обводки
# Что бы залить квадрат, в отребуте thickness указываем cv2.FILLED
cv2.rectangle(photo, (50, 50), (150, 150), (119, 201, 105), thickness=3)  # Рисуем с помощью OpenCV

# Рисуем линию
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (119, 201, 105), thickness=3)

# Рисуем круг
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (119, 201, 105), thickness=3)

# Выводим текст
cv2.putText(photo, 'itProger', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), thickness=2)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
