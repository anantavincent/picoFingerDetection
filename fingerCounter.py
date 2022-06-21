from curses import baudrate
from socket import timeout
import cv2
import mediapipe as mp
import serial

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingerCoordinates = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumbCoordinate = (4, 2)
ser = serial.Serial('COM22', baudrate = 9600, timeout=1)

while True:
    success, img = cap.read()
    imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imRGB)
    multiLandmarks = results.multi_hand_landmarks

    if multiLandmarks:
        handPoints = []
        for handLms in multiLandmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            for idx, lm in enumerate(handLms.landmark):
                # print(idx, lm)
                h,w,c = img.shape
                cx,cy = int(lm.x * w),  int(lm.y * h)
                # print(idx, cx, cy)

                handPoints.append((cx, cy))
                
        for point in handPoints:
            # print()
            # cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)
            upCount = 0

        for coordinate in fingerCoordinates:
            if handPoints[coordinate[0]][1] < handPoints[coordinate[1]][1]:
                upCount += 1

        if handPoints[thumbCoordinate[0]][0] > handPoints[thumbCoordinate[1]][0]:
            upCount += 1

        cv2.putText(img, str(upCount), (150, 150), cv2.FONT_HERSHEY_PLAIN, 12, (255, 0, 0), 12)

        if upCount == 1:
            ser.write(b'A')

        if upCount == 3:
            ser.write(b'B')

    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)
