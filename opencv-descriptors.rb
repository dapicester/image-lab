require 'ropencv'
include OpenCV

img = cv::imread 'images/vino.jpg'
gray = cv::Mat.new
cv::cvtColor img, gray, cv::COLOR_BGR2GRAY

# SIFT, SURF and BRIEF are not available because non-free
detector = cv::ORB.create
kp = Vector.new cv::KeyPoint
detector.detect gray, kp
puts "found #{kp.size} keypoints"

cv::drawKeypoints img, kp, img
cv::imshow 'descriptors', img
cv::waitKey 0
cv::destroyAllWindows
