import cv2, time
import numpy


#Motion dection function
def motionDection():
    #Video in realTime
    video = cv2.VideoCapture(0)

    ret, frame1 = video.read()
    ret, frame2 = video.read()

    while video.isOpened():
        diff = cv2.absdiff(frame1,frame2)
        
        #Convert to grayscale and gassican blur
        gray_frame = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        blur_frame = cv2.GaussianBlur(gray_frame,(21,21),0)

        _, thresh = cv2.threshold(blur_frame,20,255,cv2.THRESH_BINARY)
        thresh = cv2.dilate(thresh, None, iterations=3)

        contours,_ = cv2.findContours(
            thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )



        
       





