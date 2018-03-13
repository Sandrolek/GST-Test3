gst-launch-1.0 v4l2src device="/dev/video1" ! image/jpeg,width=800,height=600,framerate=30/1 ! \
jpegdec ! autovideosink sync=false
