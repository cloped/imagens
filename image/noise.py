import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

img = cv2.imread('Lenna.png')

lines = img.shape[0]
cols = img.shape[1]

gray_new_img = np.zeros((lines, cols))

def noise(pixel):
    x = random.randint(0, 100)

    if x > 15:
        return pixel
    return (x % 2) * 255

for i in range(0, lines):
  for j in range(0, cols):
    gray = int(img[i][j].sum() / 3)

    gray_new_img[i][j] = noise(gray)

cv2.imwrite('noisy_Lenna.jpg', gray_new_img)
