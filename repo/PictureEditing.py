##Code for editing pictures
import cv2
import numpy as np
img=cv2.imread("Resources/pic1.jpg")
kernel=np.ones((5,5),np.unit8)

imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGrey,(21,21),0)
imgCanny = cv2.Canny(img,200,200)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Blurred",imgBlur)
cv2.imshow("Output",imgGrey)
#cv2.imshow("Canny",imgCanny)
#cv2.imshow("Dialated",imgDialation)
#cv2.imshow("Eroded",imgEroded)
#cv2.waitKey(0)

