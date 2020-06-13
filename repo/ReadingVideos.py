##Code for reading videos
import cv2
video=cv2.VideoCapture("Resources/test_video.mp4")
while True:
	success, image=video.read() #Success variable is a boolean
	cv2.imshow("Video",image)
	if cv2.waitKey(1) & 0xFF==ord('s'):
		break
