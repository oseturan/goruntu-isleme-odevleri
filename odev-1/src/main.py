# ODEV 1: Cozunurluk yariya ve ceyrege indirme
import cv2

resim = cv2.imread('odev-1/input/image1.jpg', 0)
h, w = resim.shape

yari = cv2.resize(resim, (int(w / 2), int(h / 2)))
ceyrek = cv2.resize(resim, (int(w / 4), int(h / 4)))

cv2.imwrite('odev-1/output/yari_boyut.png', yari)
cv2.imwrite('odev-1/output/ceyrek_boyut.png', ceyrek)
