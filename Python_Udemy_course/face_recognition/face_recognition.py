import os

import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('C:\\Users\\DELL\\PycharmProjects\\pythonProject\\Python_Course\\Python_Udemy_course\\face_recognition\\haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

print(os.getcwd())
def insert_or_update(Id, Name, age):
    connect = sqlite3.connect("C:\\Users\\DELL\\PycharmProjects\\pythonProject\\Python_Course\\Python_Udemy_course\\face_recognition\\SQLite.db")
    cursor = connect.cursor()  # Access the cursor
    cursor.execute("SELECT * FROM STUDENTS WHERE ID = ?", (Id,))  # Use parameterized query
    is_record_exist = cursor.fetchone() is not None  # Check for existing record

    if is_record_exist:
        cursor.execute("UPDATE STUDENTS SET Name=?, age=? WHERE Id=?", (Name, age, Id))
    else:
        cursor.execute("INSERT INTO STUDENTS (Id, Name, age) VALUES(?, ?, ?)", (Id, Name, age))

    connect.commit()
    connect.close()

Id = input('Enter User Id: ')
Name = input('Enter User Name: ')
age = int(input('Enter User Age: '))

insert_or_update(Id, Name, age)

sample_num = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for x, y, w, h in faces:  # Use meaningful variable names for width and height
        sample_num += 1
        cv2.imwrite("dataset/user." + str(Id) + str(sample_num) + ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.waitKey(100)  # Wait 100 milliseconds for key press

    cv2.imshow("Face", img)
    if cv2.waitKey(1) == ord('q'):  # Break loop if 'q' is pressed
        break

    if sample_num > 20:
        break

cam.release()
cv2.destroyAllWindows()
