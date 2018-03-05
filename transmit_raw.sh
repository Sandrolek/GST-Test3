gst-launch-1.0 v4l2src device='/dev/video0' ! jpegenc ! \
rtpjpegpay ! udpsink host=127.0.0.1 port=9000

