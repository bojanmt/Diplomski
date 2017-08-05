import numpy as np
import cv2
import os, sys
import glob




count=0
for img in glob.glob("D:\dipl\Cropped area\*.jpg"): #path where raw images extracted from videos are stored
    cv_img = cv2.imread(img, 0)
    ret, thresh_img = cv2.threshold(cv_img,127,255,cv2.THRESH_BINARY)
    #cv2.imshow("binary", thresh_img)
    real_image=thresh_img
    cv2.imwrite ("d:\dipl\Binary Image\blackwhite%d.jpg" %count , real_image) 
    #cv2.imshow("cropped", crop_img)
    #cv2.waitKey(0)
    count += 1
    #height, width, channels = img.shap
    #print height, width, channels
cv2.destroyAllWindows()