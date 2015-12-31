import cv2
import matplotlib.pyplot as plt
import sys

img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)

#detector, norm = cv2.xfeatures2d.SIFT_create(), cv2.NORM_L2
detector, norm = cv2.ORB_create(), cv2.NORM_HAMMING

kp1, des1 = detector.detectAndCompute(img1, None)
kp2, des2 = detector.detectAndCompute(img2, None)

matcher = cv2.BFMatcher(norm)
matches = matcher.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good.append(m)
print("matched %d" % len(good))
img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, flags=2)
plt.imshow(img3), plt.show()
