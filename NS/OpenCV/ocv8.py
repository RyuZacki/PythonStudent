import cv2
import numpy as np

photo = cv2.imread("images/Lox.jpg")
img = np.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

# img = cv2.bitwise_and(circle, square)  # Объединение по общим чертам
# img = cv2.bitwise_or(circle, square)  # Полное объединение
# img = cv2.bitwise_xor(circle, square)  # Объединение двух объектов, но всё что совпало не было добавлено к новым изображениям
# img = cv2.bitwise_not(circle, square)  # Получаем инверсию
img = cv2.bitwise_and(photo, photo, mask=circle)  # Деалем круглый вырез

cv2.imshow("Result", img)
cv2.waitKey(0)
