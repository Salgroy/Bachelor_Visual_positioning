import cv2 as cv
cap = cv.VideoCapture(2)
cap2 = cv.VideoCapture(1)

num = 0

while cap.isOpened():
    succes1, img = cap.read()
    succes2, img2 = cap2.read()
    k = cv.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv.imwrite('stereoLeft/imageL' + str(num) + '.png', img2)
        cv.imwrite('stereoRight/imageR' + str(num) + '.png', img)
        print('images saved!')
        num +=1


    cv.imshow('Img 1',img2)
    cv.imshow('Img 2',img)

cap.release()
cap2.release()

cv.destroyAllWindows()