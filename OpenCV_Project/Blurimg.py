import cv2
import numpy as np

img = cv2.imread('Resource/luoxiang.jpg')

grey_img = cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)
# Blurring Image
blur_img = cv2.GaussianBlur(grey_img,(7,7),0)

# Edge Detector
img_Canny_100_100 = cv2.Canny(img, 100, 100)
img_Canny_150_200 = cv2.Canny(img, 150, 200) # Less detail

# Increase thickness of the edges
kernel = np.ones((3,3),np.uint8)
img_dilation = cv2.dilate(img_Canny_150_200,kernel=kernel,iterations=1)

# Decrease thickness of the edges
img_eroded = cv2.erode(img_dilation,kernel=kernel,iterations=1)


# cv2.imshow("grey",grey_img)
# cv2.imshow("blur",blur_img)
cv2.imshow("Canny 100 100", img_Canny_100_100)
cv2.imshow("Canny 150 200", img_Canny_150_200)
cv2.imshow("Image Dilation", img_dilation)
cv2.imshow("Image Eroded",img_eroded)


cv2.waitKey(0)
cv2.destroyAllWindows()