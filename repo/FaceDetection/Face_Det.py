import cv2

faceCascade=cv2.CascadeClassifier("Face_Det.xml")
Video=cv2.VideoCapture(0)
Video.set(3,640)
Video.set(4,480)

while True:
    success,img=Video.read()
    Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(Gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        break

