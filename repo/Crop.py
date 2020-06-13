##Code for cropping
import cv2
img=cv2.imread("Resources/pic1.jpg")
Cropped=img[0:200,200:500]
cv2.imshow("Normal",img)
cv2.imshow("Cropped",Cropped)
cv2.waitkey(0)
