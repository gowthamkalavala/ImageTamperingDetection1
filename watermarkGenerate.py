def generate(w, j):
    width = int(512 * w)
    height = int(512 * j)
    return (width, height)

# # Concatenate these images for ease of display using cv2.hconcat()
# finalr = cv2.hconcat([eight_bit_img, seven_bit_img])
# finalv = cv2.hconcat([six_bit_img, five_bit_img])
#
# # Vertically concatenate
# final = cv2.vconcat([finalr, finalv])
#
# # Display the images
# cv2.imshow('a', final)
# cv2.waitKey(0)
