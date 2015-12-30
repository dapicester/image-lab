require 'ropencv'
include OpenCV

img = cv::imread 'images/paolo.jpg'
cv::imshow 'paolo', img
cv::wait_key 0
cv::destroy_all_windows
