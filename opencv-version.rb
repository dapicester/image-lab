require 'ffi'
require 'ffi/tools/const_generator'
require 'ropencv'

def ffi_version
  gen = FFI::ConstGenerator.new('opencv2') do |g|
    g.include 'opencv2/core/version.hpp'
    g.const :CV_VERSION_MAJOR
    g.const :CV_VERSION_MINOR
    g.const :CV_VERSION_REVISION
  end

  "%d.%d.%d" % [gen['CV_VERSION_MAJOR'], gen['CV_VERSION_MINOR'], gen['CV_VERSION_REVISION']]
end

def pkg_config_version
  `pkg-config --modversion opencv`
end

def ropencv_version
  include OpenCV
  "%d.%d.%d" % [CV_VERSION_MAJOR, CV_VERSION_MINOR, CV_VERSION_REVISION]
end

puts "FFI: #{ffi_version}"
puts "pkg-config: #{pkg_config_version}"
puts "ropencv: #{ropencv_version}"
