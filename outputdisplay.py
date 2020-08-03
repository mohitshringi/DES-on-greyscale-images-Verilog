import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
file1 = open(r'D:\I-CHIP_2bits\ofb_enc_out.txt',
             "r+")  #opening the decrypted txt file having hex no.
test_str = file1.read()  #reading full file as a string
i = 0
b = []
a = ""
while i < 2097152:
    a = test_str[i:i + 2]  #substrings of length 2 throufhout the string
    b.append(int(a, 16))  #converting into decimal of range 0-255
    i = i + 2
arr = np.array(b)  #list to array
arr = arr.reshape(1024, 1024)  #reshaping
plt.imshow(arr, cmap="gray")  #displaying output/decrypted image
plt.show()
# images were saved using save option on bottom of plt.show() window

