import cv2              #opencv camera
import numpy as np      #numpy array
import sqlite3          #sqlite is database


faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')       #to detect the faces in camera
cam = cv2.VideoCapture(0);      # 0 is for web camera

def insert_or_update(Id, Name, age):     # function for sqlite database
    connect = sqlite3.connect("database.db")    #connet to database
    cmd = "SELECT * FROM STUDENTS WHERE ID="+str(Id);
    cursor = connect.execute(cmd)
    is_record_exist = 0         # assume there is no record in our table
    for row in cursor:
        is_record_exist = 1

    if is_record_exist == 1:
        connect.execute("UPDATE STUDENTS SET Name=? WHERE Id=?", (Name, Id,))
        connect.execute("UPDATE STUDENTS SET age=? WHERE Id=?", (age, Id))
    else:
        connect.execute("INSERT INTO STUDENTS (Id, Name, age) values(?, ?, ?)", (Id, Name, age))

    connect.commit()
    connect.close()

Id = input('Enter User Id')
Name = input('Enter User Name')
age = int(input('Enter User Age'))

insert_or_update(Id, Name, age)

# detect face in web camera coding

sample_num = 0      # assume there is no sample dataset
    ret, img = read()       # Open Camera
    gray = cv2.cvtColor(img.cv2.COLOR_BGR2GRAY)         # Image convert to bgrgray color
    faces = faceDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)      #scale face
    for x, y, width, height in faces:
        sample_num += 1
