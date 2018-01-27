import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

isopen=cv2.VideoCapture(0)
while(isopen.isOpened()):
  ret, img=isopen.read()
  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray,1.3,5)
  for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]
    cv2.imshow('temp',roi_color)
    
    cv2.imshow('img',img)
  if cv2.waitKey(10) & 0xFF == ord('q'):
     isopen.release()
cv2.destroyAllWindows()