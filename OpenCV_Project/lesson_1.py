import cv2

# import a video
cap = cv2.VideoCapture("Resource/sex.MP4")

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



