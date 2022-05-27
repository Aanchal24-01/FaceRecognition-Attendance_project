# FaceRecognition-Attendance_project
This is a real-time **face recognition project** with **tracking  Attendance** made **using Python -OpenCv** 


**Objective-->**

->As FaceRecognition deals with the matching of facial features by recognizing face-distance.OpenCV library in Python,
uses machine learning algorithms to search for faces within a picture. 

->So,in this project it recognises the face of a person using webcam and track live attendance in ** Excel sheet**

**Prerequirement -->**

1.Install python,git,OpenCV,cv2,cmake,dlib(according to your python version),Numpy and face recognition library .

2.It will recognise the face of a person whose image is present in the folder **imagesAttendance (i.e Elon Musk,Indira Gandhi,Mahatma Gandhi,Sundar-Pichai)**
therefore, if you want to track someone else attendace then fistly feed the image of that person in that folder.

**Working -->**

You can go through the file **basics.py** for the general idea of working of this software that is as follow

-I have divided the project in 3 parts :-_
![Screenshot (84)](https://user-images.githubusercontent.com/85822746/170771348-f1287f0a-3228-44c2-afc3-ca64a3f9f8a9.png)

->firstly I will import the imgaes so that it can get converted into rgb

->secondly I will find the encoding of both the images(first from the folder **imagesAttendance** and second one from the webcam)

->thirdly I will campare the encodings of both the image ,if it get matched then it will show "true" with face-distance .
![Screenshot (85)](https://user-images.githubusercontent.com/85822746/170771396-d191b150-2a52-49a0-9a74-8a230c69bcac.png)

************************************************

**__STEPS:-_**

Now you can run the project by following these steps:-

1.Run the file **AttendaceProject.py**
![Screenshot (82)_LI](https://user-images.githubusercontent.com/85822746/170770332-ce8a9611-935f-4e77-b27d-d79766a3ea26.jpg)

2.Show the image of the person (one of the person whose name is present in imageAttendace folder)in the front of webcam.**for example**-Mahatma Gandhi
![Screenshot (81)](https://user-images.githubusercontent.com/85822746/170769335-99e59faf-aedc-4369-b763-5b9c8d492937.png)

3.In attendanceProject, firstly, images of the person are imported then encodings of the images are found out by findEncodings() function.
![encoding](https://user-images.githubusercontent.com/85822746/170772384-cae15c72-959b-4e9f-9070-4260ba531b34.PNG)

4.After that by accesiing webcam another image is taken with encoding of the second image and then comparision is done
![comparison](https://user-images.githubusercontent.com/85822746/170772429-c3d51c8e-40db-4b47-a914-2ae3d2404ca7.PNG)

5.Images are examined and marked through the function markAttendnace() and their live attendance is marked in a Attendance.csv file time with name and .
![markatten](https://user-images.githubusercontent.com/85822746/170772478-823e4261-e0bf-4161-8cf2-2f32b9512214.PNG)

OUTPUT-
![output](https://user-images.githubusercontent.com/85822746/170772609-cf75c12b-3e9a-4c33-a16b-f639f8e636bc.PNG)





