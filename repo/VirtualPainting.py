import cv2
import numpy as np
Video=cv2.VideoCapture(0)
Video.set(3,640)
Video.set(4,480)
Video.set(10,150)

myColours=[77,113,124,255,53,158]
mc=[255,132,10]
mypts=[]

def findColor(imgResult):
    imgHSV=cv2.cvtColor(imgResult,cv2.COLOR_BGR2HSV)
    lower = np.array([77,124,53])
    upper = np.array([113,255,158])
    newp=[]
    mask = cv2.inRange(imgHSV, lower, upper)
    x,y=getContours(mask)
    cv2.circle(imgResult,(x,y),10,(255,132,10),cv2.FILLED)
    if x!=0 and y!=0:
        newp.append([x,y])
    #cv2.imshow("img",mask)
    return newp


def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(img,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            #print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawing(mypts):
    for point in mypts:
        cv2.circle(imgResult,(point[0],point[1]),10,(255,0,0),cv2.FILLED)

while True:
    success,imgResult=Video.read()
    newpts=findColor(imgResult)
    if len(newpts)!=0:
        for nep in newpts:
            mypts.append(nep)
    if len(mypts)!=0:
        drawing(mypts)

    cv2.imshow("result",imgResult)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        break






