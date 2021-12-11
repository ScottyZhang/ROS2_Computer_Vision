import cv2
import numpy as np
"""
Bird eye view
"""

card_img = cv2.imread('Resource/cards.jpeg')

width,height = 250,350

# 1. Define four corner points of the card
# pt1 = (1080,550)
# pt2 = (435,950)
# pt3 = (800,1170)
# pt4 = (1430,770)
pts1 = np.float32([[1080,550],[1430,770],[435,950],[800,1170]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# 2. Get the transformation matrix
matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

# 3. Warp the Image
img_output = cv2.warpPerspective(card_img,matrix,(width,height))




cv2.imshow("Cards",img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()