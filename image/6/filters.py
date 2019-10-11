import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randint

img = cv2.imread('./6/gray_lenna.png')

lines = img.shape[0]
cols = img.shape[1]

ruido_sal = np.zeros((lines, cols))
ruido_pimenta = np.zeros((lines, cols))
ruido = np.zeros((lines, cols))

mean_lenna_filter_ruido_sal = np.zeros((lines, cols))
median_lenna_filter_ruido_sal = np.zeros((lines, cols))
mean_lenna_filter_ruido_pimenta = np.zeros((lines, cols))
median_lenna_filter_ruido_pimenta = np.zeros((lines, cols))
mean_lenna_filter_ruido = np.zeros((lines, cols))
median_lenna_filter_ruido = np.zeros((lines, cols))

def calc_mean(image, i, j, limit):
  p = 0
  p += 4 * image[i][j]
  p += 2 * image[i-1][j] + image[i][j-1] + image[i+1][j] + image[i][j+1]
  p += image[i-1][j-1] + image[i-1][j+1] + image[i+1][j-1] + image[i+1][j+1]
  
  gray_pixel = p // 16

  if abs(gray_pixel - image[i][j]) > limit:
    return image[i][j]
  
  return gray_pixel


def calc_median(image, i, j):
  p = []
  p.append(image[i][j])
  p.append(image[i-1][j])
  p.append(image[i][j-1])
  p.append(image[i+1][j])
  p.append(image[i][j+1])
  p.append(image[i-1][j-1])
  p.append(image[i+1][j+1])
  p.append(image[i+1][j-1])
  p.append(image[i-1][j+1])

  # gray_pixel = np.median(p)
  gray_pixel = np.min(p)
  # gray_pixel = np.max(p)
  return gray_pixel

LIMIT = 300

for i in range(1, lines - 1):
  for j in range(1, cols - 1):
    rand = randint(0, 100)
    if rand <= 5: # 20%
      ruido_sal[i][j] = 255 # sal
      ruido_pimenta[i][j] = 0  # pimenta
      # if 
    else:
      ruido_sal[i][j] = img[i][j][0]
      ruido_pimenta[i][j] = img[i][j][0]

    if rand == 1:
      ruido[i][j] = 255
    elif rand == 2:
      ruido[i][j] = 0
    else:
      ruido[i][j] = img[i][j][0]
    
    mean_lenna_filter_ruido_sal[i][j] = calc_mean(ruido_sal, i, j, LIMIT)
    median_lenna_filter_ruido_sal[i][j] = calc_median(ruido_sal, i, j)

    mean_lenna_filter_ruido_pimenta[i][j] = calc_mean(ruido_pimenta, i, j, LIMIT)
    median_lenna_filter_ruido_pimenta[i][j] = calc_median(ruido_pimenta, i, j)

    mean_lenna_filter_ruido[i][j] = calc_mean(
        ruido, i, j, LIMIT)
    median_lenna_filter_ruido[i][j] = calc_median(ruido, i, j)

cv2.imwrite('./6/ruido_sal.png', ruido_sal)
cv2.imwrite('./6/mean_lenna_filter_ruido_sal.png',
            mean_lenna_filter_ruido_sal)
cv2.imwrite('./6/median_lenna_filter_ruido_sal.png',
            median_lenna_filter_ruido_sal)

cv2.imwrite('./6/ruido_pimenta.png', ruido_pimenta)
cv2.imwrite('./6/mean_lenna_filter_ruido_pimenta.png',
            mean_lenna_filter_ruido_pimenta)
cv2.imwrite('./6/median_lenna_filter_ruido_pimenta.png',
            median_lenna_filter_ruido_pimenta)

cv2.imwrite('./6/ruido.png', ruido)
cv2.imwrite('./6/mean_lenna_filter_ruido.png',
            mean_lenna_filter_ruido)
cv2.imwrite('./6/median_lenna_filter_ruido.png',
            median_lenna_filter_ruido)
