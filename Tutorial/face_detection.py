import cv2

def face_detection():
    """
    1. convert image to gray scale
    2. load the classifier
    3. detection
    4. draw a box
    """
    gray_img = cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)
    face_detect = cv2.CascadeClassifier('/home/huairui/opencv-master/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gray_img,1.01,5,0,(100,100),(300,300))
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv2.imshow('result',img)

img = cv2.imread('./luoxiang.jpg')
face_detection()

cv2.waitKey(0)
cv2.destroyAllWindows()