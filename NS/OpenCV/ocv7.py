import cv2
import numpy as np

img = cv2.imread('images/lox.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

cv2.imshow('result', img)
cv2.waitKey(0)
