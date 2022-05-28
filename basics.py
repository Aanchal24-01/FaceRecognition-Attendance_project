import cv2
from cv2 import COLOR_BGR2RGB
import numpy as np
import face_recognition

#first -import the images and convert them into rgb
imgElon=face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest=face_recognition.load_image_file('ImagesBasic/Elon Test.jpg')
imgeTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

#second-

#encoding for Elon
faceLoc=face_recognition.face_locations(imgElon)[0]
encodeElon=face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(250,0,0),2)
#encoding for elon test
faceLocTest=face_recognition.face_locations(imgTest)[0]
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(250,0,0),2)


#third-comparing the encoding of both(distance between the two images)
results=face_recognition.compare_faces([encodeElon],encodeTest)
faceDis=face_recognition.face_distance([encodeElon],encodeTest)

#printing the result and face distance 
print(results,faceDis)
cv2.putText(imgTest,f'{results}{round(faceDis[0],4)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Test',imgTest)
cv2.waitKey(0)

