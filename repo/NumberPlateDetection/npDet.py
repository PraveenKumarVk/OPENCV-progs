import cv2
img1=cv2.imread("npp.png")
npCascade=cv2.CascadeClassifier("np.xml")
minArea=100
area=0


imgGray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
numberplates = npCascade.detectMultiScale(imgGray)

for (x,y,w,h) in numberplates:
    area=w*h

    if area>minArea:
        cv2.rectangle(img1,(x,y),(x+w,y+h),(20,150,255),3)
        cv2.putText(img1,"NUMBER PLATE",(x,y-5),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,0.5,(0,0,255),1)
        imgRoi=img1[y:y+h,x:x+w]
        cv2.imshow("ROI",imgRoi)
    print(area)

cv2.imshow("Result",img1)
cv2.waitKey(0)
