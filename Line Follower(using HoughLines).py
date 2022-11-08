import cv2
import numpy as np
import math
vid=cv2.VideoCapture(1)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)
vid.set(cv2.CAP_PROP_FPS, 25)
while True:
    ret,frame=vid.read()
    cv2.imshow('new',frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(gray,(5,5),0)
    edges=cv2.Canny(blurred,80,80)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=5)
    theta=0;

    for x in range(0,len(lines)):
        a=lines[x]
        x1,y1,x2,y2=a[0]
        cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),3)
        theta=math.atan2((y2-y1),(x2-x1))
        threshold=4
        cv2.imshow('TEST',edges)
        print(theta)
        if theta>threshold:        
            print("Go Right")
        if abs(theta)>threshold:
            print("Go Left")
        else:
            print("Go straight")
    if cv2.waitKey(1) &  0xFF==ord('q'):
        break
''' else:
        cv2.imshow('new',frame)
        if cv2.waitKey(1) &  0xFF==ord('q'):
            break'''
                
           
vid.release()
cv2.destroyAllWindows()
    
    
    