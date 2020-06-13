import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img=cv2.imread('qr.jpg')
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,380)

with open('text.txt') as f:
    DList=f.read().splitlines()
print(DList)

while True:
    success,img=cap.read()
    for barcode in decode(img):
        Data = barcode.data.decode('utf-8')

        if Data in DList:
            myOp='Authorized'
            myColor=(0,255,0)
        else:
            myOp='Unauthorized'
            myColor=(0,0,255)
        pts=np.array([barcode.polygon])
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),1)
        pts2=barcode.rect
        cv2.putText(img,myOp,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_PLAIN,0.9,myColor,1)

    cv2.imshow('result',img)
    cv2.waitKey(1)

