import cv2
import numpy as np
import sys
import sqlite3
from func_for_db import get_name_person

face_cas = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('/dev/video0')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('data/trainer/trainer.yml')
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        uid, conf=recognizer.predict(roi_gray)
        info_person = get_name_person(uid)
        cv2.putText(img, info_person[0], (x,y-10), font, 0.55, (120,255,120), 1)
    cv2.imshow('frame', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
cap.release()
cv2.destroyAllWindows()

