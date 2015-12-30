import cv2

img = cv2.imread('images/vino.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SIFT, SURF and BRIEF are not available because non-free
detector = cv2.ORB_create()
kp = detector.detect(gray, None)
print("found {size} keypoints".format(size=len(kp)))

img = cv2.drawKeypoints(img, kp, None)
cv2.imshow("descriptors", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
