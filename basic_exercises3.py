import cv2 

################################################################
#做影像處理時常用得函式

img = cv2.imread('LOGO1.jpg')#讀取圖片


#把BGR的圖片轉換成灰階圖片
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#把圖片變模糊效果

blur = cv2.GaussianBlur(gray,(5,5),0)#GauassianBlur(圖片函數,((5,5)是合了5*5的圖片),標準差)

#取得圖片的邊緣

canny = cv2.Canny(blur,50,150)#Canny(圖片函数,邊緣閥値,邊緣閥値)

#把圖片膨脹

dilate = cv2.dilate(canny,None,iterations=1)#dilate(圖片函数,None,iterations=1)

#把圖片侵蝕

erode = cv2.erode(dilate,None,iterations=1)#erode(圖片函数,None,iterations=1)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)


cv2.waitKey(0)#等完畢關閉
