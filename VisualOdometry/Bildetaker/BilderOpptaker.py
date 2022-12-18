import cv2
import time

#Setter in hvilke kameraer som skal benytte
cap1 = cv2.VideoCapture(1) 
cap2 = cv2.VideoCapture(2)

#Teller bilder
num = 0

#Kvalitet paa bidlene i x og y retning
cap1.set(3, 720)
cap1.set(4, 480)
cap2.set(3, 720)
cap2.set(4, 480)

#Setter opp parametre
old_frame_left = None
old_frame_right = None
new_frame_left = None
new_frame_right = None

while(cap1.isOpened() and cap2.isOpened()): #While lokke for naar kameraeneopptak er aktivert

    ret1, new_frame_left = cap1.read() #oversetter verdier fra kamera til new_frame_ parametre
    ret2, new_frame_right = cap2.read()
    
    old_frame_left = new_frame_left    #Lagrer nytt bilde til gammelt bilde
    old_frame_right = new_frame_right
#imageL' + og imageR'
    cv2.imwrite('stereoLeft/' + str(num) + '.png', old_frame_left)  #Lagrer bildene i Left/Right mappene med bildetall
    cv2.imwrite('stereoRight/' + str(num) + '.png', old_frame_right)#For at bildene lagres i rekkefolge
    num +=1
    
    #Viser bildene paa skjerm
    cv2.imshow("img", new_frame_left)
    cv2.imshow("img2", new_frame_right)
    
    #Denne bestemmer hvor mange FPS bildene blir tatt i. 0.0025 ms tilsvarer 20 FPS
    time.sleep(0.025)

    #Avslutter opptaket med tast 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()

cv2.destroyAllWindows()