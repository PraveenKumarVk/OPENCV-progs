##Code for using WebCam
import cv2
video=cv2.VideoCapture(0)
#video.set(3,640)
#video.set(4,480)  ##3 and 4 are symbols for length and width
#video.set(10,130) ##10 is used to adjust brightness
while True:
	success, image=video.read() #Success variable is a boolean
	cv2.imshow("Video",image)
	if cv2.waitKey(1) & 0xFF==ord('s'):
		break