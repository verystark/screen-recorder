import pyautogui
import cv2
import numpy as np

# Creating the VideoWriter object
resolution = (1920, 1080)
codec = cv2.VideoWriter.fourcc(*'XVID')
filename = 'recording.mp4'
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Making an empty window to show the recording in real time
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

# Infinite loop that takes a screenshot in every iteration and writes it to the output file
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    
    # Displays the recording screen in real time
    cv2.imshow('Live', frame)
    
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

out.release()

cv2.destroyAllWindows()



