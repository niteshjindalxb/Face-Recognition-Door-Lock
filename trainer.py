import cv2
import os
import numpy as np
from PIL import Image

recognizer=cv2.face.createLBPHFaceRecognizer();
path = 'Train'

def getimage(path):
    imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagepath in imagepaths:
        faceimage=Image.open(imagepath)
        facenp=np.array(faceimage,'uint8')
        gray=cv2.cvtColor(facenp,cv2.COLOR_BGR2GRAY)
        ID=int(os.path.split(imagepath)[-1].split('.')[1])
        faces.append(gray)
        print(ID)
        IDs.append(ID)
        cv2.imshow("training",facenp)
        cv2.waitKey(100)
    return IDs,faces
Ids,faces=getimage(path)
recognizer.train(faces,np.array(Ids))
recognizer.save('abcd.yml')
recognizer.load('abcd.yml')
cv2.destroyAllWindows()