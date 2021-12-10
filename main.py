import cv2
import numpy as np

def Rose_test():
    rose_img = cv2.imread('./rose.jpg') # rose_img is a array
    print(rose_img.shape)
    #print(type(rose_img))
    print(rose_img) # 3-D Array (height weight BGR)

    # cv2.imshow('rose',rose_img)
    # cv2.imshow('rose',rose_img[:,:,::-1])
    cv2.imshow('rose',rose_img-255)



    cv2.waitKey() # w8ing key Input to close the window
    cv2.destroyWindow() # release RAM

def py_check():
    a = np.uint8(-9)
    print(a)


if __name__ == '__main__':
    Rose_test()
    # py_check()
