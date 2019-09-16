import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lenna.png')

lines = img.shape[0]
cols = img.shape[1]

# new_img = np.zeros((lines, cols, 3))
gray_new_img = np.zeros((lines, cols))

def equalization(pixel):
    if pixel <= 75:
        # return pixel // 2
        return 0
    if pixel < 175:
        return 2 * pixel - 127
    # return pixel // 2 + 127 
    return 255

for i in range(0, lines):
  for j in range(0, cols):
    # blue = img[i][j][0]
    # red = img[i][j][1]
    # green = img[i][j][2]
    gray = int(img[i][j].sum() / 3)

    # equalization(blue)
    # equalization(red)
    # equalization(green)
    

    # new_img[i][j] = [blue, red, green]
    gray_new_img[i][j] = equalization(gray)

# cv2.imwrite('equalization.jpg', new_img)
cv2.imwrite('gray_equalization.jpg', gray_new_img)
