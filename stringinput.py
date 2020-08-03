import cv2
import numpy as np

img = cv2.imread(r'D:\I-CHIP_2bits\image.jpg', 0)
img = cv2.resize(img, (int(1024), int(1024)))
n = np.array(img)
a = []
for i in n:
    for v in i:
        a.append('{0:08b}'.format(v))
a = np.array(a)

delimiter = ''

st = delimiter.join(a)

st = np.array([st])
np.savetxt(r'D:\I-CHIP_2bits\input.txt', st, fmt='%s')
