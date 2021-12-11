import cv2
import numpy as np
path = 'Resource/lambo.jpeg'

def empty(a):
    pass

# Creat a track bar
cv2.namedWindow("Track bar")
cv2.resizeWindow("Track bar",1000,640)
cv2.createTrackbar("Hue Min","Track bar",0,179,empty)
cv2.createTrackbar("Hue Max","Track bar",179,179,empty)
cv2.createTrackbar("Sat Min","Track bar",0,255,empty)
cv2.createTrackbar("Sat Max","Track bar",255,255,empty)
cv2.createTrackbar("Val Min","Track bar",0,255,empty)
cv2.createTrackbar("Val Max","Track bar",255,255,empty)



while True:
    img = cv2.imread(path)
    hsv_img = cv2.cvtColor(img,code=cv2.COLOR_BGR2HSV)
    # Get Track bar values
    h_min = cv2.getTrackbarPos("Hue Min","Track bar")
    h_max = cv2.getTrackbarPos("Hue Max","Track bar")
    s_min = cv2.getTrackbarPos("Sat Min","Track bar")
    s_max = cv2.getTrackbarPos("Sat Max","Track bar")
    v_min = cv2.getTrackbarPos("Val Min","Track bar")
    v_max = cv2.getTrackbarPos("Val Max","Track bar")

    hsv_mat = np.array([h_min,h_max,s_min,s_max,v_min,v_max])

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(hsv_img,lower,upper)


    # cv2.imshow("Original",img)
    cv2.imshow("HSV",hsv_img)
    cv2.imshow("Mask",mask)
    cv2.waitKey(1)

