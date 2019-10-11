import cv2
import numpy as np

img = cv2.imread('Lenna.png')
new_img = cv2.imread('Lenna.png')

lines = img.shape[0]
cols = img.shape[1]

for i in range(0, lines):
  for j in range(0, cols):
    new_img[i][j] = 255 - new_img[i][j]

cv2.imwrite('./2/negative.jpg', new_img)
