import cv2
import numpy as np


img = np.zeros((600,600,3),np.uint8)#黑圖片框

#畫一條直線
cv2.line(img,(0,0),(400,300),(0,255,0),1)#line(圖片框,(起始座標),(終點座標),線色,粗度)


#畫一條線從左上角到右下角

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),1)#img.shape[] 1為圖片寬度，2為圖片的高度

#畫一個方形

cv2.rectangle(img,(200,200),(500,500),(0,0,255),1)#rectangle(圖片框,(角1),(角2),線色,粗度)
#如果要把方形顏色填滿

cv2.rectangle(img,(0,0),(200,200),(0,0,255),cv2.FILLED)#rectangle(圖片框,(角1),(角2),線色,線填滿)

#畫一個圓形

cv2.circle(img,(400,400),30,(255,255,0),1)#circle(圖片框,(圓心),半大小,線色,粗度)
#把圓形填滿顏色

cv2.circle(img,(300,300),30,(255,255,0),cv2.FILLED)#circle(圖片框,(圓心),半大小,線色,線填滿)

#寫上文字
cv2.putText(img,'Hello World',(300,300),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)#putText(圖片框,(文字),左上角對應的像素

cv2.imshow('img',img)#顧示圖片
cv2.waitKey(0)#等完關閉

