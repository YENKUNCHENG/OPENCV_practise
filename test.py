import cv2

# img = cv2.imread(r'C:\Users\hynpq\OneDrive\文件\Java\作品\python\LOGO1.jpg')#讀取圖片或影片路徑，前面要加r，如果要讀取視訊設備則是輸入數字

# cv2.imshow('LOGO1',img)

# cv2.waitKey(0)

cap = cv2.VideoCapture(0)#讀取圖片或影片路徑，前面要加r，如果要讀取視訊設備則是輸入數字


while True:
    
    ret,frame =cap.read()

    if ret:
        cv2.imshow('frame',frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break