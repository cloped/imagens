import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lenna.png')

lines = img.shape[0]
cols = img.shape[1]

gray_new_img = np.zeros((lines, cols))
new_img = np.zeros((lines, cols, 3))

def border(pixel):
    return 4 * (pixel // 4)

for i in range(0, lines):
  for j in range(0, cols):
    blue = img[i][j][0]
    red = img[i][j][1]
    green = img[i][j][2]
    gray = int(img[i][j].sum() / 3)

    new_img[i][j] = [border(blue), border(red), border(green)]
    gray_new_img[i][j] = border(gray)

def vGradiente(image, i, j):
  img = (image[i][j] - image[i+1][j+1]) ** 2 + (image[i][j+1] - image[i+1][j]) ** 2
  for k in range(3) :
    if (img[k] >= 300):
      img[k] = image[i][j][k]
    else:
      img[k] = 0
  return img

def gradiente(image, i, j):
  img = (image[i][j] - image[i+1][j+1]) ** 2 + (image[i][j+1] - image[i+1][j]) ** 2
  if (img >= 300):
    # return img
    return 255
  # return image[i][j]
  return 0

for i in range(0, lines - 1):
  for j in range(0, cols - 1):
    new_img[i][j] = vGradiente(new_img, i, j)
    gray_new_img[i][j] = gradiente(gray_new_img, i, j)

for i in range(0, lines):
  new_img[cols - 1][i] = new_img[i][lines - 1] = 0
  gray_new_img[cols - 1][i] = gray_new_img[i][lines - 1] = 0

cv2.imwrite('border.jpg', new_img)
cv2.imwrite('gray_border.jpg', gray_new_img)
