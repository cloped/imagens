import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lenna.png')

max_size = 256 * 4
histogram_red = np.zeros(max_size)
histogram_green = np.zeros(max_size)
histogram_blue = np.zeros(max_size)

histogram_gray = np.zeros(max_size)

lines = img.shape[0]
cols = img.shape[1]

def histogram(img, p) :
    blue = img[i][j][0]
    red = img[i][j][1]
    green = img[i][j][2]
    gray = int(img[i][j].sum() / 3)

    histogram_blue[blue + p] += 1
    histogram_red[red + p] += 1
    histogram_green[green + p] += 1
    histogram_gray[gray + p] += 1


for i in range(0, lines // 2):
    for j in range(0, cols // 2):
        histogram(img, 0)

for i in range(0, lines // 2):
    for j in range(cols // 2, cols):
        histogram(img, 256)

for i in range(lines // 2, lines):
    for j in range(0, cols // 2):
        histogram(img, 512)

for i in range(lines // 2, lines):
    for j in range(cols // 2, cols):
        histogram(img, 768)


fig = plt.figure()
plt.plot(histogram_red, color='red')
fig.savefig('red_local_histogram.png')

fig = plt.figure()
plt.plot(histogram_green, color='green')
fig.savefig('green_local_histogram.png')

fig = plt.figure()
plt.plot(histogram_blue, color='blue')
fig.savefig('blue_local_histogram.png')

fig = plt.figure()
plt.plot(histogram_gray, color='gray')
fig.savefig('gray_local_histogram.png')

fig = plt.figure()
plt.plot(histogram_red, color='red')
plt.plot(histogram_green, color='green')
plt.plot(histogram_blue, color='blue')
fig.savefig('rgb_local_histogram.png')
