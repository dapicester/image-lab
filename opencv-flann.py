import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)

# detector, norm = cv2.xfeatures2d.SIFT_create(), cv2.NORM_L2
detector, norm = cv2.ORB_create(), cv2.NORM_HAMMING

kp1, des1 = detector.detectAndCompute(img1, None)
kp2, des2 = detector.detectAndCompute(img2, None)

FLANN_INDEX_KDTREE = 1
FLANN_NUM_TREES = 5
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=FLANN_NUM_TREES)
search_params = dict(checks=50)
matcher = cv2.FlannBasedMatcher(index_params, search_params)
# XXX: here assertion fails in OpenCV cv2 Python module.
matches = matcher.knnMatch(np.asarray(des1, np.float32), np.asarray(des2, np.float32), k=2)

matchesMask = [[0, 0] for i in xrange(len(matches))]
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7 * n.distance:
        matchesMask[i] = [1, 0]

MIN_MATCH_COUNT = 10
good = len([x for x in matchesMask if x == [1, 0]])
print("Found good %d matches" % good)

if good < MIN_MATCH_COUNT:
    print("Not enough matches: %d/%d" % (good, MIN_MATCH_COUNT))
    matchesMask = None

draw_params = dict(matchColor=(0,255,255),
                singlePointColor=None,
                matchesMask=matchesMask,
                flags=2)
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, **draw_params)
plt.imshow(img3), plt.show()
