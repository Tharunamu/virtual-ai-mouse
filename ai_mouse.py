import mediapipe as mp
import cv2
import numpy as np
from math import sqrt
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
click = 0

# Adjust cursor speed and sensitivity
pyautogui.FAILSAFE_DELAY = 0.001
pyautogui.PAUSE = 0.001

video = cv2.VideoCapture(0)  # Use camera index 0 for the default built-in camera

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        imageHeight, imageWidth, _ = image.shape
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )

        if results.multi_hand_landmarks is not None:
            for handLandmarks in results.multi_hand_landmarks:
                thumb_tip = handLandmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = handLandmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                thumb_tip_x, thumb_tip_y = int(thumb_tip.x * imageWidth), int(thumb_tip.y * imageHeight)
                index_tip_x, index_tip_y = int(index_tip.x * imageWidth), int(index_tip.y * imageHeight)

                try:
                    # Adjust cursor movement sensitivity
                    scaling_factor = 3  # Adjust the scaling factor as needed
                    cursor_x = int(index_tip_x * scaling_factor)
                    cursor_y = int(index_tip_y * scaling_factor)
                    pyautogui.moveTo(cursor_x, cursor_y)

                    distance = sqrt((thumb_tip_x - index_tip_x) ** 2 + (thumb_tip_y - index_tip_y) ** 2)
                    if distance < 30:
                        click += 1
                        if click % 5 == 0:
                            print("Click gesture detected")
                            pyautogui.click()  # Perform the click action

                except:
                    pass

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows() 
