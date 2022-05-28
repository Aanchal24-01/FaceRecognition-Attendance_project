from base64 import encode
import cv2
from cv2 import COLOR_BGR2RGB
from cv2 import FILLED
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np
import face_recognition
import os
from datetime import datetime

#creating list for the images so we dont have to write manually each time 
path='imagesAttendance'
images=[]
classNames=[]
myList=os.listdir(path)

#printing the list
print(myList)

#importing images one by one using for loop
for cl in myList:
   curImg=cv2.imread(f'{path}/{cl}')
   images.append(curImg)
   #we are appending here so that list  will not get printed with extension 
   classNames.append(os.path.splitext(cl)[0])

#printing the list again 
print(classNames)

# till  now we have found our image  now we have to find the encodings of the image using the findEncodings( ) function
def findEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

#for tracking the attendace in excel sheet
def markAttendence(name):
    with open('Attendance.csv','r+') as f:
        myDataList=f.readlines()
        nameList=[]
        for line in myDataList:
           entry=line.split(',')
           nameList.append(entry[0])
        if name not in nameList:
            now =datetime.now()
            dtString=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

#to run the function findEncodings calling is done here
encodeListKnown=findEncodings(images)

#to find it works properly print here
print('Encoding Complete')

#as we dont have second image to have encoding to campre with fisrt one it will come from webcam
cap=cv2.VideoCapture(0)

while True:
    success,img=cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    #to tackle the case in wich we are goinf to find miultiple images in webcam we will firstly find the location of that image
    facesCurFrame=face_recognition.face_locations(imgS)
    encodesCurFrame=face_recognition.face_encodings(imgS,facesCurFrame)

    #after getting encoding of both the imges here we are matching them
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex=np.argmin(faceDis)

        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            #calling attendace function
            markAttendence(name)

    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
    
