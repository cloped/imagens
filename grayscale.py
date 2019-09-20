import cv2
import numpy as np

img = cv2.imread('Lenna.png')

lines = img.shape[0]
cols = img.shape[1]

new_img = np.zeros((lines, cols))

for i in range(0, lines):
  for j in range(0, cols):
    brg_grayscale = img[i][j].sum() / 3
    new_img[i][j] = brg_grayscale

cv2.imwrite('gray_lenna.png', new_img)

