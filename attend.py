import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64
from tkinter import*

root = Tk()
root.geometry("845x435")
root.title("Attendence Using QR Code")
root.configure(background="#CD00CD")
Label(text = "",background="#CD00CD").pack()
Label(text = "",background="#CD00CD").pack()
Label(text = "",background="#CD00CD").pack()
Label(text = "",background="#CD00CD").pack()
Label(text = "",background="#CD00CD").pack()
Label(text = "",background="#CD00CD").pack()
Label(text = "",background="#CD00CD").pack()

def qrattend():
    #Start Web Cam
    cap = cv2.VideoCapture(0)

    names = []


    #Function For Attendence File
    fob = open('attendence.txt','a+')
    def enterData(z):
        if z in names:
            pass
        else:
            names.append(z)
            z="".join(str(z))
            fob.write(z + '\n')
            return names

    print('Reading Code...')


    #Function Data Present Or Not
    def checkData(data):
        data = str(data)
        if data in names:
            print('Already Present')
        else:
            print(str(len(names)+1) + '\n' + 'Present Done')
            enterData(data)

    while True:
        _,frame = cap.read()
        decodedObject = pyzbar.decode(frame)
        for obj in decodedObject:
            checkData(obj.data)
            time.sleep(1)

    cv2.imshow('Frame', frame)


    #close
    if cv2.waitKey(1) & 0xff==ord('s'):
        cv2.destoryAllWindows()

    fob.close()

Button(text = "Take Attendence Using QR Code", font = "Algerian", height = "4", width = "50", command = qrattend, bg="#B23AEE", fg="#F0F8FF").pack()

root.mainloop()
