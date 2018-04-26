import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('one_roof.jpg',0)

# make image brighter
alpha = 1
beta = 70
img = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)

# apply GaussianBlur filter
img = cv2.GaussianBlur(img,(5,5),0)

# apply canny edge detection
edges = cv2.Canny(img,115,30)

# plot before and after images
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()


