import cv2
import numpy as np

def size_blackwhite():
    rose = cv2.imread('./rose.jpg')

    #change size
    resized_rose = cv2.resize(rose,(300,182))

    cv2.imshow('resized',resized_rose)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def change_blackwhite():
    rose = cv2.imread('./rose.jpg')
    gray_rose = cv2.cvtColor(rose, code = cv2.COLOR_BGR2GRAY) #black and white pic
    cv2.imshow('Grey', gray_rose)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def chang_HSV():
    rose = cv2.imread('./rose.jpg')
    HSV_rose = cv2.cvtColor(rose, code=cv2.COLOR_BGR2HSV)  #
    cv2.imshow('HSV', HSV_rose)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # size_blackwhite()
    change_blackwhite()
    chang_HSV()