# ODEV 4: 1024x768 Boyutlandirma
import cv2

resim = cv2.imread('odev-4/input/image1.jpg')
boyut = cv2.resize(resim, (1024, 768))
cv2.imwrite('odev-4/output/gorsel_1024x768.png', boyut)
