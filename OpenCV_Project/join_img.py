import cv2
import numpy as np

"""
Put all the img in one window
"""

img = cv2.imread('Resource/luoxiang.jpg')

# stack the images horizontally
hor_img = np.hstack((img,img))

# stack the images vertical
var_img = np.vstack((img,img))

"""
both images need to be exactly same matrix size
"""

cv2.imshow("Hor",hor_img)
cv2.imshow("Ver",var_img)
cv2.waitKey(0)
cv2.destroyAllWindows()