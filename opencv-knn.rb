require 'ropencv'
include OpenCV

img1 = cv::imread ARGV.shift, cv::IMREAD_GRAYSCALE
img2 = cv::imread ARGV.shift, cv::IMREAD_GRAYSCALE

#detector, norm = cv::SIFT.new, cv::NORM_L2
detector, norm = cv::ORB.create, cv::NORM_HAMMING

kp1 = Vector.new cv::KeyPoint
kp2 = Vector.new cv::KeyPoint
des1 = cv::Mat.new(3, 4, cv::CV_64FC1)
des2 = cv::Mat.new(3, 4, cv::CV_64FC1)

detector.detect_and_compute img1, cv::Mat.new, kp1, des1
detector.detect_and_compute img2, cv::Mat.new, kp2, des2

matcher = cv::BFMatcher::new norm
matches = Vector.new Vector.new cv::DMatch
matcher.knn_match des1, des2, matches, 2

good = Vector.new cv::DMatch
matches.each do |match|
  m, n = match[0], match[1]
  good << m if m.distance < 0.7 * n.distance
end
puts "matched #{good.count}"

img_matches = cv::Mat.new 3, 4, cv::CV_64FC1
cv::draw_matches img1, kp1, img2, kp2, good, img_matches, cv::Scalar::all(-1), cv::Scalar::all(-1), Vector::Char.new(), 2
cv::imshow 'matches', img_matches
cv::wait_key 0
