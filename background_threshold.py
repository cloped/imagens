import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lenna.png')

lines = img.shape[0]
cols = img.shape[1]

gray_new_img = np.zeros((lines, cols))

def background_threshold(pixel):
    return pixel * (pixel > 127) 

for i in range(0, lines):
  for j in range(0, cols):
    gray = int(img[i][j].sum() / 3)

    gray_new_img[i][j] = background_threshold(gray)

cv2.imwrite('gray_background_threshold.jpg', gray_new_img)
