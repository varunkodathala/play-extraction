import cv2
import numpy as np

video_path = '/Users/varun/Documents/Deep_Learning/Learn_PYTORCH/TRAJECTORY/video3.mp4'

cam = cv2.VideoCapture(video_path)

i = 0
font  = cv2.FONT_HERSHEY_SIMPLEX
while(True):

    ret,frame = cam.read()
    fps = cam.get(cv2.CAP_PROP_FPS)
    cv2.imshow('frame',frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    if(i>0):
        difference = cv2.subtract(blur, temp_blur)
        ret,thresh_diff = cv2.threshold(difference,20,255,cv2.THRESH_BINARY)
        cv2.putText(thresh_diff,f"fps: {round(fps)}",(10,40), font, 1,(255,255),2,cv2.LINE_AA)
        cv2.putText(difference,f"fps: {round(fps)}",(10,40), font, 1,(255,255),2,cv2.LINE_AA)
        cv2.imshow("thresh_diff",thresh_diff)
        cv2.imshow("Difference",difference)

        temp_blur = blur
    else:
        temp_blur = blur

    i+=1

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
    

cv2.destroyAllWindows()