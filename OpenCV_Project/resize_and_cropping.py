import cv2
import numpy as np

org_img = cv2.imread("Resource/lambo.jpeg")
print(org_img.shape)


# Resize the Image
dsize = np.array([300,200])
img_resize = cv2.resize(org_img,dsize=dsize)

print(img_resize.shape)

# Crop the Image
img_crop = org_img[200:500, 500:900] # First Height, then width

cv2.imshow("Origin lambo",org_img)
# cv2.imshow("Resized lambo",img_resize)
cv2.imshow("Croped lambo",img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()