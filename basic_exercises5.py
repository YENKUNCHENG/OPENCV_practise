import cv2
import numpy as np

def empty(v):
    pass
#邊緣顏色檢測
################################################################

img = cv2.imread('2.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

#做一個動態條視窗來找出顏色的值
cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar',640,320)

cv2.createTrackbar('Hue Min','Trackbar',0,179, empty)
cv2.createTrackbar('Hue Max','Trackbar',179,179, empty)
cv2.createTrackbar('Sat Min','Trackbar',0,255, empty)
cv2.createTrackbar('Sat Max','Trackbar',255,255, empty)
cv2.createTrackbar('Val Min','Trackbar',0,255, empty)
cv2.createTrackbar('Val Max','Trackbar',255,255, empty)

#先把圖片BGR圖片轉成HSV圖片
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#取得控制條數值
while True:
    h_min = cv2.getTrackbarPos('Hue Min','Trackbar')
    h_max = cv2.getTrackbarPos('Hue Max','Trackbar')
    s_min = cv2.getTrackbarPos('Sat Min','Trackbar')
    s_max = cv2.getTrackbarPos('Sat Max','Trackbar')
    v_min = cv2.getTrackbarPos('Val Min','Trackbar')
    v_max = cv2.getTrackbarPos('Val Max','Trackbar')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    
    mask =cv2.inRange(hsv,lower,upper)
    reslut = cv2.bitwise_and(img,img,mask=mask)
    
    
    
    
    
    
    
    cv2.imshow('img',img)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('reslut',reslut)
    
    cv2.waitKey(1)
   








################################################################