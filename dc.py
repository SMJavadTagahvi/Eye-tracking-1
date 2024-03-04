import cv2
import time
import numpy as np
from datetime import datetime

cap = cv2.VideoCapture(0)
i = 0
points = [(8, 8), (8, 250), (8, 465), (325, 8), (325, 250), (325, 465), (625, 8), (625, 250), (625, 465)]
def move_circle():
    global x, y
    x += 100
    y += 100
for point in points:
    for _ in range(3):  
        

        path = '1.png'
    
        # Reading an image in grayscale mode 
        image = cv2.imread(path, 0) 
        time.sleep(1)
        cv2.rectangle (image, pt1=(0,1), pt2 =(1,1), color=(0, 0, 0), thickness=-1)
        time.sleep(1)

        
        ret, frame = cap.read()
        time.sleep(1)
        cv2.imwrite(f"point_{point}.jpg", frame)
        # filename = f'image_{datetime.now().strftime("%Y%m%d_%H%M%S")}_{i}.jpg'
        # cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
 
        windowName = 'frame'
        cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WND_PROP_FULLSCREEN)
        
        if ret:
            cv2.rectangle (frame, pt1=(0,500), pt2 =(800,1), color=(0, 0, 0), thickness=-1)
            cv2.circle(frame, point, 8, (255, 255, 255), -1)
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
                    
cap.release()

cv2.destroyAllWindows()
