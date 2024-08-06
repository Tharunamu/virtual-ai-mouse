Virtual AI Mouse
This project uses MediaPipe and OpenCV to create a virtual mouse controlled by hand gestures. The code captures video from the webcam, tracks hand landmarks, and uses thumb and index finger movements to move the cursor and perform click actions.

Prerequisites
Python 3.x
OpenCV
MediaPipe
PyAutoGUI
Installation
Clone this repository or download the source code.

Install the required libraries using pip:
pip install opencv-python mediapipe pyautogui

How to Run
Open a terminal or command prompt.

Navigate to the directory where the script is located.

Run the script:
python virtual_ai_mouse.py

Ensure your webcam is connected and working.

The program will start capturing video from the default webcam (camera index 0).

Move your thumb and index finger to control the mouse cursor.

Perform a click gesture by bringing your thumb and index finger close together.

Code Explanation

The script performs the following tasks:

Import Libraries: Imports the necessary libraries: MediaPipe, OpenCV, NumPy, Math, and PyAutoGUI.

Initialize MediaPipe and PyAutoGUI: Sets up the MediaPipe Hands solution for hand tracking and configures PyAutoGUI for mouse control.

Capture Video: Starts capturing video from the default webcam.

Hand Landmark Detection: Processes each video frame to detect hand landmarks using MediaPipe.

Cursor Movement: Calculates the position of the index finger tip and moves the cursor accordingly.

Click Detection: Measures the distance between the thumb tip and the index finger tip to detect a click gesture.

Display Video: Displays the video feed with hand landmarks drawn.

Exit Condition: Stops the program when the 'q' key is pressed.

Adjustments

Cursor Sensitivity: You can adjust the scaling_factor variable to change the sensitivity of cursor movement.
Click Gesture Sensitivity: You can modify the distance threshold in the click detection logic to change the sensitivity of the click gesture.
Troubleshooting
Ensure your webcam is working and accessible.
Make sure you have installed all the required libraries.
Adjust the detection confidence thresholds if the hand landmarks are not being detected reliably.
Contact
For any questions or suggestions, please contact Tharun at stharun612@gmail.com.
