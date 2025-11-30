import cv2 
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(2) 
background = cv2.imread('./image.jpg')

if background is None:
    print("Error: 'image.jpg' not found. Please ensure the file exists.")
    exit()

while cap.isOpened():
    ret, current_frame = cap.read()
    if ret:
        
        # --- FIX FOR SIZE MISMATCH ERROR ---
        # 1. Get the height and width (w, h) of the live frame.
        h, w, c = current_frame.shape
        
        # 2. Resize the static background image to match the live frame size.
        background = cv2.resize(background, (w, h))
        # ----------------------------------
        
        # converting from rgb to hsv color space
        hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        # --------------------------------------------------------
        # DARK BLUE RANGE
        # --------------------------------------------------------
        # H: 100-130, S: 80-255, V: 10-180
        lower_blue = np.array([100, 80, 10])
        upper_blue = np.array([130, 255, 180])
        
        # Creating the blue mask
        blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
        # --------------------------------------------------------

        # Morphology to remove noise
        kernel = np.ones((3, 3), np.uint8)
        blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel, iterations=2)
        
        # Dilate to increase the mask size slightly
        blue_mask = cv2.dilate(blue_mask, kernel, iterations=1)

        # Substituting the blue portion with background image
        # This line now works because 'background' and 'blue_mask' have the same size.
        part1 = cv2.bitwise_and(background, background, mask=blue_mask)

        # Detecting the non-blue part
        blue_free = cv2.bitwise_not(blue_mask)

        # Show the current image where the cloak is not present
        part2 = cv2.bitwise_and(current_frame, current_frame, mask=blue_free)

        # Final output
        cv2.imshow("cloak", part1 + part2)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()