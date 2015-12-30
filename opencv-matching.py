import cv2
import matplotlib.pyplot as plt
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

img1 = cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(file2, cv2.IMREAD_GRAYSCALE)

# detector, norm = cv2.xfeatures2d.SIFT_create(), cv2.NORM_L2
detector, norm = cv2.ORB_create(), cv2.NORM_HAMMING

kp1, des1 = detector.detectAndCompute(img1, None)
kp2, des2 = detector.detectAndCompute(img2, None)

matcher = cv2.BFMatcher(norm, crossCheck=True)

matches = matcher.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)

img3=cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None)
plt.imshow(img3), plt.show()
