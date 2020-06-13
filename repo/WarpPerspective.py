import cv2
img=cv2.imread("Resources/cards.jpg")
width,height=400,600
pts1=np.float32([[210,62],[254,97],[154,133],[197,167]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOp=cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Op",imgOp)
cv2.waitKey(0)
