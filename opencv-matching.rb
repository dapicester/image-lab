require 'ropencv'
include OpenCV

img1 = cv::imread ARGV.shift, cv::IMREAD_GRAYSCALE
img2 = cv::imread ARGV.shift, cv::IMREAD_GRAYSCALE

kp1 = Vector.new cv::KeyPoint
kp2 = Vector.new cv::KeyPoint
des1 = cv::Mat.new(3, 4, cv::CV_64FC1)
des2 = cv::Mat.new(3, 4, cv::CV_64FC1)

#detector, norm = cv::SIFT.new, cv::NORM_L2
detector, norm = cv::ORB.create, cv::NORM_HAMMING

detector.detect_and_compute img1, cv::Mat.new, kp1, des1
detector.detect_and_compute img2, cv::Mat.new, kp2, des2

matcher = cv::BFMatcher::new norm, true
matches = Vector.new cv::DMatch
matcher.match des1, des2, matches

img_matches = cv::Mat.new 3, 4, cv::CV_64FC1
top_matches = Vector.new(*matches.to_a[0..10])
cv::draw_matches img1, kp1, img2, kp2, top_matches, img_matches
cv::imshow 'matches', img_matches
cv::wait_key 0
