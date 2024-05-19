import cv2


# GStreamer pipeline for CSI camera on Jetson Nano
pipeline_str = (
    "nvarguscamerasrc sensor_id=0 ! "
    "video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)NV12, framerate=(fraction)30/1 ! "
    "nvvidconv ! "
    "video/x-raw, format=(string)BGRx ! "
    "videoconvert ! "
    "video/x-raw, format=(string)BGR ! "
    "appsink"
)

pipeline_str2 = (
    "nvarguscamerasrc sensor_id=1 ! "
    "video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)NV12, framerate=(fraction)30/1 ! "
    "nvvidconv ! "
    "video/x-raw, format=(string)BGRx ! "
    "videoconvert ! "
    "video/x-raw, format=(string)BGR ! "
    "appsink"
)

# Create OpenCV VideoCapture object with GStreamer pipeline
cap = cv2.VideoCapture(pipeline_str, cv2.CAP_GSTREAMER)
cap2 = cv2.VideoCapture(pipeline_str2, cv2.CAP_GSTREAMER)

# Check if the camera opened successfully
if not (cap.isOpened() and cap2.isOpened()):
    print("Error: Could not open camera.")
    exit()

num = 0

while True:
   
    succes1, img = cap.read()
    succes2, img2 = cap2.read()


    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('images/stereoLeft/imageL' + str(num) + '.png', img)
        cv2.imwrite('images/stereoRight/imageR' + str(num) + '.png', img2)
        print("images saved!")
        num += 1

    cv2.imshow('Img 1',img)
    cv2.imshow('Img 2',img2)

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
