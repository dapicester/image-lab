import cv2

img = cv2.imread('images/paolo.jpg')
cv2.imshow('paolo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
