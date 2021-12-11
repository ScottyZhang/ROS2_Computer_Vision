import cv2
import numpy as np
"""
1. Create a Matrix filled with 0s -> Black
2. Add another channel to the Matrix
3. Color the Image
4. Create line
5. Create rectangle
6. Fill the area
7. Create circle
8. Put text
"""
# 1.
# img = np.zeros((512,512))

# 2. cv2 deals with img with first height then width
# But draw something is first width then height
img = np.zeros((512,512,3),np.uint8)

# 3.
# img[:] = 255,0,0 # [:] means color the whole image

# 4.
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),color=(0,255,0),thickness=2)

# 5. 6.
x,y,w,h = 100,150,50,60
cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,255,255),thickness=2)

# 7.
cv2.circle(img,(300,100),50,color=(255,255,0),thickness=2)

# 8.
cv2.putText(img,"OpenCV",(200,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),2)


cv2.imshow("Image",img)
print(img.shape)




cv2.waitKey(0)
cv2.destroyAllWindows()