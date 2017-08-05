
import numpy as np
import cv2

#print(cv2.__version__) - used to detect the version; it was necessary so cv2.VideoCapture would work; you need to edit .dll files; look up on google

vidcap = cv2.VideoCapture("d:\\dipl\\test.wmv")
count = 0 #frame counter in a video
while (vidcap.isOpened()):

    ret, frame = vidcap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("img%d.jpg" %count, frame) #saving frame as JPEG file
    cv2.imshow('frame',gray)
#    if cv2.waitKey(0) & 0xFF == ord('q'):
       # break
    count += 1
cap.release()
cv2.destroyAllWindows()