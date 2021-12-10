import cv2

def draw_shape():
    img = cv2.imread('./luoxiang.jpg')
    print(img.shape)
    # Coordinate
    x,y,w,h = 365,184,100,100
    # Draw Rectangle
    cv2.rectangle(img,(x,y,w,h),color=(0,0,255),thickness=1)
    # Draw Circle
    cv2.circle(img,center=(x+w,y+h),radius=100,color=(255,0,0),thickness=2)

    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    draw_shape()