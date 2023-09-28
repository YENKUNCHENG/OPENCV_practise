import cv2


#輪廓檢測
img = cv2.imread('3.jpg')
imgContour = img.copy()


ing = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#把圖片變成GARY
canny  = cv2.Canny(ing,100,200)#把圖片變成灰階，檢測邊緣
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#找圖片輪廓

for cnt in contours:
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)#畫出輪廓的線
    area = cv2.contourArea(cnt)
    if area > 500:
        # print(cv2.arcLength(cnt, True))
        peri = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
        corners = len(vertices)
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 4)
        if corners == 3:
            cv2.putText(imgContour, 'triangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 4:
            cv2.putText(imgContour, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 5:
            cv2.putText(imgContour, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners >= 6:
            cv2.putText(imgContour, 'circle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)    



cv2.imshow('image',img)
cv2.imshow('canny',canny)
cv2.imshow('imgContour',imgContour)
cv2.waitKey(0)
