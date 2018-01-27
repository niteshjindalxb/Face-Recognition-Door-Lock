import cv2
import numpy as np
import serial
import time
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ser = serial.Serial('COM6', 9600, timeout=0)
isopen=cv2.VideoCapture(0)
rec=cv2.face.createLBPHFaceRecognizer()
rec.load('pqrs.yml')
time=0
count=0
id=0
while(isopen.isOpened()):
  for time in range(0,30):
    ret, img=isopen.read()
    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
      cv2.imshow('img',img)
      id,conf=rec.predict(gray[y:y+h,x:x+w])
      print (id)
      if id==1:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        count=count+0.035
        if count>=1 :
          ser.write(b'v')
          time.sleep(7)
          
      cv2.imshow('img',img)                   
  count=0     
    
  if cv2.waitKey(10) & 0xFF == ord('q'):
    isopen.release()
    cv2.destroyAllWindows()
