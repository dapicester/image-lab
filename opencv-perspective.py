import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/vino.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[121,153], [368,152], [148,481], [345,487]])
pts2 = np.float32([[0,0], [247, 0], [0, 300], [247,370]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (247, 370))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
