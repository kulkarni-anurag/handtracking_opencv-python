import numpy as np
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while(True):
    #Capture frame by frame
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    #Display the resulting frame
    cv2.imshow('Image', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#When everything done release the capture
cap.release()
cv2.destroyAllWindows()