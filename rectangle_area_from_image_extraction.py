import numpy as np
import cv2
import os, sys
import glob



#current_path='D:\dipl\Regular images' #path where raw images extracted from videos are stored
#new_path="d:\dipl\cropped area" #path where we'll store frames extracted from each image
count=0
for img in glob.glob("D:\dipl\Gray\*.jpg"): #path where gray images are
    cv_img = cv2.imread(img)
    crop_img = cv_img[70:392, 350:650] #y:y+h ; x:x+w ; from top left corner to bottom right corner ; top left corner being 0,0
    cv2.imwrite ("d:\dipl\cropped area\parts%d.jpg" %count , crop_img) #path where cropped images are store
    #cv2.imshow("cropped", crop_img)
    #cv2.waitKey(0)
    count += 1
    #height, width, channels = img.shape
    #print height, width, channels
cv2.destroyAllWindows()






##region = I[248:280,245:288]



#current_path='D:\dipl\Regular images' #path where raw images extracted from videos are stored
#new_path="d:\dipl\Extracted rectangles" #path where we'll store frames extracted from each image

#listing=os.listdir(current_path) #returns list with names of files in the directory
#count=0;
#for file in listing: #loop within which we process each image and save it in a new directory
  #  img=cv2.imread("d:\dipl\gray\img0.jpg") #%count) #opens the current image
    #img = cv2.imread(current_path + file) 
  #  width, height = img.size
   # print "Dimensions:", img.size
    #count +=1 

#cv2.destroyAllWindows()

#if cv2.waitKey(0) & 0xFF == ord('q'):
       #break


#img_in_place=True

#while (img_in_place)
