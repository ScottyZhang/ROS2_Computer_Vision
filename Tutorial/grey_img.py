import cv2

if __name__ == '__main__':
    img = cv2.imread('./luoxiang.jpg')
    img = cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)

    cv2.imshow('grey_img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()