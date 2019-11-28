import numpy as np
import cv2

two_bit_img = np.array([0 for i in range(512 * 512)], dtype=np.uint8).reshape(512, 512)


def substitute(rstart, rend, cstart, cend, arr):
    two_bit_img[rstart:rend, cstart:cend] = arr


def generateWM2(img):
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
    three_bit_img = (np.array([int(i[5]) for i in lst], dtype=np.uint8) ).reshape(img.shape[0], img.shape[1])

    # substitute(0, 64, 0, 64, eight_bit_img)
    # substitute(0, 64, 128, 192, eight_bit_img)

    dict={8:eight_bit_img,7:seven_bit_img,6:six_bit_img,5:five_bit_img,4:four_bit_img,3:three_bit_img}
    array = [[8, 7, 8, 7, 8, 7, 8, 7],
             [7, 6, 5, 6, 5, 6, 5, 8],
             [8, 5, 4, 3, 4, 3, 6, 7],
             [7, 6, 3, 4, 3, 4, 5, 8],
             [8, 5, 4, 3, 4, 3, 6, 7],
             [7, 6, 3, 4, 3, 4, 5, 8],
             [8, 5, 6, 5, 6, 5, 6, 7],
             [7, 8, 7, 8, 7, 8, 7, 8]]
    for i in range(8):
        for j in range(8):
            substitute(i*64,(i+1)*64,j*64,(j+1)*64,dict[array[i][j]])
    return two_bit_img