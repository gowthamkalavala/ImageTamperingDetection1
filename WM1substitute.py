import numpy as np
import cv2

one_bit_img = np.array([0 for i in range(512 * 512)], dtype=np.uint8).reshape(512, 512)


def substitute(rstart, rend, cstart, cend, arr):
    one_bit_img[rstart:rend, cstart:cend] = arr

def generateWM1(img):
    lst = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            lst.append(np.binary_repr(img[i][j], width=8))  # width = no. of bits


    # We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
    # Multiply with 2^(n-1) and reshape to reconstruct the bit image.
    eight_bit_img = (np.array([int(i[0]) for i in lst], dtype=np.uint8) ).reshape(img.shape[0], img.shape[1])
    seven_bit_img = (np.array([int(i[1]) for i in lst], dtype=np.uint8) ).reshape(img.shape[0], img.shape[1])
    six_bit_img = (np.array([int(i[2]) for i in lst], dtype=np.uint8) ).reshape(img.shape[0], img.shape[1])
    five_bit_img = (np.array([int(i[3]) for i in lst], dtype=np.uint8) ).reshape(img.shape[0], img.shape[1])
    four_bit_img = (np.array([int(i[4]) for i in lst], dtype=np.uint8) ).reshape(img.shape[0], img.shape[1])
    three_bit_img = (np.array([int(i[5]) for i in lst], dtype=np.uint8)).reshape(img.shape[0], img.shape[1])

    dict = {8: eight_bit_img, 7: seven_bit_img, 6: six_bit_img, 5: five_bit_img, 4: four_bit_img, 3: three_bit_img}

    array=[[8,3,6,7],
           [5,4,3,4],
           [4,3,4,5],
           [7,6,3,8]]

    for i in range(4):
        for j in range(4):
            substitute(i*128,(i+1)*128,j*128,(j+1)*128,dict[array[i][j]])



    return one_bit_img
