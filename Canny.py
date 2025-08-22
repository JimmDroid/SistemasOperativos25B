import cv2

img = cv2.imread('Carta.jpg',0)
bordeCanny = cv2.Canny(img, 100,200)


