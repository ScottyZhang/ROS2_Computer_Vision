import cv2
import numpy as np

def hsv_detection():

    img1 = cv2.imread('./Tutorial_test.png')
    hsv_img = cv2.cvtColor(img1, code=cv2.COLOR_BGR2HSV) # getting HSV Image
    hsv_img = cv2.resize(hsv_img,(600,600))

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    # Mark where is blue in the Image
    mask = cv2.inRange(hsv_img,lower_blue,upper_blue)

    # Bitwise-AND mask and origin image
    # res_img = cv2.bitwise_and(img1,img1,mask = mask)



    # cv2.imshow('origin',img1)
    cv2.imshow('mask',mask)
    # cv2.imshow('res_img',res_img)

    # cv2.imshow('hsv_img',hsv_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    hsv_detection()