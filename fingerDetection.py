import cv2
import time
import os
import Hand_Tracking_Module as htm

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.75)

tipIds = [ 4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)


    print(lmList)

    cv2.imshow("Image", img)
    cv2.waitKey(1)