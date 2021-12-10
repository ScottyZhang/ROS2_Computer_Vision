import cv2
import numpy as np

if __name__ == '__main__':
    a = np.array([1,2,3,4,5])
    b = np.array([1,4,5,7,5])

    c = np.bitwise_and(a,b)

    print(bin(2))
    print(bin(4))
    print(c)