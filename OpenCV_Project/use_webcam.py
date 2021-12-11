import cv2

cap = cv2.VideoCapture(0) # default laptop webcam
cap.set(3,640) # set width (3)
cap.set(4,480) # set height (4)
cap.set(10,100) # set brightness (10)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # When press 'q', stop the video
        break
  