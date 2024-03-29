import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lenna.png')

max_size = 256
histogram_red = np.zeros(max_size)
histogram_green = np.zeros(max_size)
histogram_blue = np.zeros(max_size)

histogram_gray = np.zeros(max_size)

lines = img.shape[0]
cols = img.shape[1]

for i in range(0, lines):
  for j in range(0, cols):
    blue = img[i][j][0]
    red = img[i][j][2]
    green = img[i][j][1]
    gray = int(img[i][j].sum() / 3)

    histogram_blue[blue] += 1
    histogram_red[red] += 1
    histogram_green[green] += 1
    histogram_gray[gray] += 1

fig = plt.figure()
plt.plot(histogram_red, color='red')
fig.savefig('./3/red_histogram.png')

fig = plt.figure()
plt.plot(histogram_green, color='green')
fig.savefig('./3/green_histogram.png')

fig = plt.figure()
plt.plot(histogram_blue, color='blue')
fig.savefig('./3/blue_histogram.png')

fig = plt.figure()
plt.plot(histogram_gray, color='gray')
fig.savefig('./3/gray_histogram.png')

fig = plt.figure()
plt.plot(histogram_red, color='red')
plt.plot(histogram_green, color='green')
plt.plot(histogram_blue, color='blue')
fig.savefig('./3/rgb_histogram.png')

print([
    list(histogram_red),
    list(histogram_green),
    list(histogram_blue),
    list(histogram_gray),
])
