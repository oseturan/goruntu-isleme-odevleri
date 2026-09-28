# ODEV 3: Kuantalama (Quantization)
import cv2
import numpy as np

resim = cv2.imread('odev-3/input/image1.jpg', 0)
satir, sutun = resim.shape
cikis = np.zeros((satir, sutun), dtype=np.uint8)

for i in range(satir):
    for j in range(sutun):
        cikis[i, j] = int(resim[i, j] // 4) * 4

cv2.imwrite('odev-3/output/kuantalama_sonuc.png', cikis)
