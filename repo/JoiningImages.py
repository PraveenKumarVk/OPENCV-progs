##Code for joining images
import cv2
img=cv2.imread("Resources/cards.jpg")
imgHor=np.hstack((img,img))
imgVer=np.vstack((img,img))

cv2.imshow("Hor",imgHor)
cv2.imshow("ver",imgVer)
cv2.waitKey(0)