import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from math import sqrt, log2
from scipy.spatial import distance

limit = 0

def diff_color(img, i, j, m, n):
  resp = True

  # if abs(int(img[i][j][0])-int(img[m][n][0])) <= limit and abs(int(img[i][j][1])-int(img[m][n][1])) <= limit and abs(int(img[i][j][2])-int(img[m][n][2])) <= limit:
  #   resp = False

  # difference = sqrt((int(img[i][j][0])-int(img[m][n][0])) ** 2 + (int(img[i][j][1])-int(img[m][n][1])) ** 2 + (int(img[i][j][2])-int(img[m][n][2])) ** 2)
  difference = int(np.linalg.norm(img[i][j] - img[m][n]))
  # difference = distance.euclidean(img[i][j], img[m][n])
  if difference <= 0:
    resp = False

  return resp

# print('Done quantizing')
# cv2.imwrite('./8/teste_quantize.jpg', quantized)

def calc_histogram(image):
  img = cv2.imread(image)
  lines = img.shape[0]
  cols = img.shape[1]

  quantized = np.zeros((lines, cols, 3))
  segmented = np.zeros((lines, cols, 3))

  bins = 64
  histogram_border = np.zeros(bins)
  histogram_interior = np.zeros(bins)


  for i in range(0, lines):
    for j in range(0, cols):
      quantized[i][j] = img[i][j] // bins

  for i in range(1, lines - 1, 1):
    for j in range(1, cols - 1, 1):
      if(diff_color(quantized, i-1, j, i, j) or diff_color(quantized, i, j-1, i, j) or
        diff_color(quantized, i+1, j, i, j) or diff_color(quantized, i, j+1, i, j)):
        segmented[i][j] = [0, 0, 0] # Borda
      else:
        segmented[i][j] = [255, 255, 255] # Interior

      #############################

      mapped_int = int(quantized[i][j][0]) * 16 + \
          int(quantized[i][j][1]) * 4 + int(quantized[i][j][2])

      if segmented[i][j][0] == 0: # borda
        histogram_border[mapped_int] += 1
      else: # interior
        histogram_interior[mapped_int] += 1

  print('Done segment and histograms')
  cv2.imwrite('./8/segment.jpg', segmented)

  histogram_total = np.concatenate(
      (histogram_border, histogram_interior), axis=None)
      
  return histogram_total

base = calc_histogram('./8/data/carro1.jpg')
best_fit = calc_histogram('./8/data/carro3.jpg')
bad_fit = calc_histogram('./8/data/carro4.jpg')

def array_to_log(arr):
  return np.array([x if x <= 1 else log2(x) for x in arr])


best_fit = np.absolute(array_to_log(base) - array_to_log(best_fit)).sum()
bad_fit = np.absolute(array_to_log(base) - array_to_log(bad_fit)).sum()

print(best_fit)
print(bad_fit)
