import numpy as np
import cv2

from WM1substitute import generateWM1
from WM2substitute import generateWM2
from watermarkGenerate import generate
# Read the image in greyscale
img = cv2.imread('testImages/lena.png', 0)


img= cv2.resize(img,(512,512), interpolation = cv2.INTER_AREA)



# WaterMark 1
dim=generate(0.25,0.25)
WM1= cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# WaterMark 2
dim=generate(0.125,0.125)
WM2= cv2.resize(img, dim, interpolation = cv2.INTER_AREA)




# Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(img[i][j], width=8))  # width = no. of bits

# We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
# Multiply with 2^(n-1) and reshape to reconstruct the bit image.
eight_bit_img = (np.array([int(i[0]) for i in lst], dtype=np.uint8) * 128).reshape(img.shape[0], img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst], dtype=np.uint8) * 64).reshape(img.shape[0], img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst], dtype=np.uint8) * 32).reshape(img.shape[0], img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst], dtype=np.uint8) * 16).reshape(img.shape[0], img.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst], dtype=np.uint8) * 8).reshape(img.shape[0], img.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst], dtype=np.uint8) * 4).reshape(img.shape[0], img.shape[1])
two_bit_img = generateWM2(WM2)
one_bit_img = generateWM1(WM1)
cv2.imshow('a', one_bit_img)
cv2.waitKey(0)


