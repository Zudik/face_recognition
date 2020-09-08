import cv2
import os
import sqlite3
from func_for_db import update_db  
		     
count = 0
face_id = input('enter your id: \t')  
face_name = input('enter your name: \t')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

update_db(face_id, face_name)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        full_path_with_name = 'data/faces/' + str(face_id) + '_' + str(count) + '.jpg' 
        cv2.imwrite(full_path_with_name, gray[y:y+h,x:x+w])
    cv2.imshow('img', img)
    # Key ESC for stop
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    if count == 100:
    	print('Success')
    	break
cap.release()
cv2.destroyAllWindows()

