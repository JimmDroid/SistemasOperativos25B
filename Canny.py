## creado por jaime uriel fonseca mexia
## 22/08/2025
import cv2

img = cv2.imread('Carta.jpg',0)
bordeCanny = cv2.Canny(img, 100,200)

cv2.imshow('Original', img)
cv2.imshow('blur', bordeCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()

