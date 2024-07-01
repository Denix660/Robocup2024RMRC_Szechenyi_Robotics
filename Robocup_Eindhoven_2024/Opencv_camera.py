import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)
    if cv.waitKey(0) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

