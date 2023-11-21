import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# define the initial values for the circle
color = (0,255,0)
line_width = 3
radius = 60
point = (0,0)

'''
This function is called whenever the mouse is clicked on the video feed.
Every time we click with the left button, it will set a new point. 
'''
def click(click, x, y, flags, param):
	global point, pressed
	if click == cv2.EVENT_LBUTTONDOWN:
		print("Pressed",x,y)
		point = (x,y)

# MUST use the same name as the window that we define below
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click)

while(True):
	ret, frame = cap.read()

	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	# use the inital values to draw the circle
	cv2.circle(frame, point, radius, color, line_width)
	cv2.imshow("Frame",frame)

	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()