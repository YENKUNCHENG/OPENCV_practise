import random
import cv2

################################################################
#圖片跟陣列關係

# img = cv2.imread('LOGO1.jpg')#讀取圖片
# print(img)#顯示圖片的圖片陣列
# print(img.shape)#顯示各個屬性
# print(img.size)#顯示圖片的大小
# print(img.dtype)#顯示圖片的型態
# print(type(img))#型態
# print(img.shape)#陣列值
########################################################################
#
# import numpy as np
# img = np.empty((300,300,3),np.uint8)#創建基礎圖片框

# # for row in range(300):
# #     for col in range(300):
# #         img[row,col]=(255,0,0)#填入圖片框

# # for row in range(300):
# #     for col in range(300):
# #         img[row,col]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]#隨機顏色填入圖片框


# cv2.imshow('img',img)#顧示圖片
# cv2.waitKey(0)
########################################################################
#切割圖片

img = cv2.imread('LOGO1.jpg')#讀取圖片

img_crop = img[0:200,0:200]#切副各個屬性

cv2.imshow('img',img)#顧示圖片

cv2.imshow('img_crop',img_crop)#顧示切前套圖片

cv2.waitKey(0)

########################################################################
