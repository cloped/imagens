import cv2
import numpy as np

img = cv2.imread('Lenna.png')

histogram_red = np.zeros(255)
histogram_green = np.zeros(255)
histogram_blue = np.zeros(255)
histogram_gray = np.zeros(255)

lines = img.shape[0]
cols = img.shape[1]

new_img = np.zeros((lines, cols))

for i in range(0, lines):
  for j in range(0, cols):
    brg_grayscale = img[i][j].sum() / 3
    new_img[i][j] = brg_grayscale

cv2.imwrite('andre.jpg', new_img)

