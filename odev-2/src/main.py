# ODEV 2: Pikselleri donguyle gezme ve (0.75 * piksel + 20) islemi
import cv2
import numpy as np

resim = cv2.imread('odev-2/input/image1.jpg', 0)
satir, sutun = resim.shape
cikis = np.zeros((satir, sutun), dtype=np.uint8)

for i in range(satir):
    for j in range(sutun):
        deger = int(resim[i, j] * 0.75 + 20)
        if deger > 255:
            cikis[i, j] = 255
        elif deger < 0:
            cikis[i, j] = 0
        else:
            cikis[i, j] = deger

cv2.imwrite('odev-2/output/parlaklik_sonuc.png', cikis)
