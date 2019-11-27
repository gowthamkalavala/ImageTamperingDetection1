import numpy as np
import cv2
def generateWM1(img):
 lst=[]
 for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(img[i][j], width=8))  # width = no. of bits

 one_bit_img =np.array([0 for i in range(512*512)], dtype=np.uint8).reshape(512,512)


 # We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
# Multiply with 2^(n-1) and reshape to reconstruct the bit image.
 eight_bit_img = (np.array([int(i[0]) for i in lst], dtype=np.uint8) * 128).reshape(img.shape[0], img.shape[1])
 seven_bit_img = (np.array([int(i[1]) for i in lst], dtype=np.uint8) * 64).reshape(img.shape[0], img.shape[1])
 six_bit_img = (np.array([int(i[2]) for i in lst], dtype=np.uint8) * 32).reshape(img.shape[0], img.shape[1])
 five_bit_img = (np.array([int(i[3]) for i in lst], dtype=np.uint8) * 16).reshape(img.shape[0], img.shape[1])
 four_bit_img = (np.array([int(i[4]) for i in lst], dtype=np.uint8) * 8).reshape(img.shape[0], img.shape[1])
 three_bit_img = (np.array([int(i[5]) for i in lst], dtype=np.uint8) * 4).reshape(img.shape[0], img.shape[1])



 one_bit_img[0:128,0:128]=eight_bit_img
 one_bit_img[0:128,128:256]=three_bit_img
 one_bit_img[0:128,256:384]=six_bit_img
 one_bit_img[0:128,384:512]=seven_bit_img


 one_bit_img[128:256,0:128]=five_bit_img
 one_bit_img[128:256,128:256]=four_bit_img
 one_bit_img[128:256,256:384]=three_bit_img
 one_bit_img[128:256,384:512]=four_bit_img


 one_bit_img[256:384,0:128]=four_bit_img
 one_bit_img[256:384,128:256]=three_bit_img
 one_bit_img[256:384,256:384]=four_bit_img
 one_bit_img[256:384,384:512]=five_bit_img

 one_bit_img[384:512, 0:128] = seven_bit_img
 one_bit_img[384:512, 128:256] = six_bit_img
 one_bit_img[384:512, 256:384] = three_bit_img
 one_bit_img[384:512, 384:512] = eight_bit_img



 return one_bit_img





