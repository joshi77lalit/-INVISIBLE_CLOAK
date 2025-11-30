#import the opencv  library for image processing 
import cv2 

#creating an object to capture vedion 
cap = cv2.VideoCapture(0)

#getting the back-ground image
while cap.isOpened():
  ret, background = cap.read()
  if ret:
      cv2.imshow("image",background)
      if cv2.waitKey(5)  == ord('q'):
        cv2.imwrite("image.jpg",background)
        break

cap.release()
cv2.destroyAllWindows()