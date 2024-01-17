import cv2 as cv
import numpy as np

#############################################################
#يمكن تعديل الباراميترات بحسب الحاجة
############################################################33

image = cv.imread('C:\\Users\\CEC\\Desktop\\im15.jpg')
image = cv.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
image_copy = image.copy()
gray = cv.cvtColor(image_copy, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (7,7),0)
thresh = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,11,28)
kernel = cv.getStructuringElement(1, (11,3))
dilate = cv.dilate(thresh, kernel, iterations=13)
cnts = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv.contourArea(c)
    if area > 1000:
        x,y,w,h = cv.boundingRect(c)
        cv.rectangle(image_copy, (x, y), (x + w, y + h), (36,255,12), 3)
cv.imshow('dilate', dilate)
cv.imshow('image', image_copy)
dst =cv.inpaint(image,dilate,3,cv.INPAINT_TELEA)
cv.imshow('dst', dst)
cv.waitKey()