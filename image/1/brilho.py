import cv2
import numpy as np

img = cv2.imread('Lenna.png')
lines = img.shape[0]
cols = img.shape[1]

new_img = np.zeros((lines, cols, 3))

lines = img.shape[0]
cols = img.shape[1]

for i in range(0, lines):
  for j in range(0, cols):
    for k in range(0,3):
      soma = -100
      aux = img[i][j][k] + soma
      if img[i][j][k] + soma < 0:
        aux = 0
      if img[i][j][k] + soma > 255:
        aux = 255
      new_img[i][j][k] = aux

cv2.imwrite('./1/brilho.jpg', new_img)
