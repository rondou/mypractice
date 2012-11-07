import cv
import sys
alpha = 0.8
beta = 0.8
image_1 = cv.LoadImageM(r"C:\Documents and Settings\rondou.chen\My Documents\Downloads\480_1.PNG")
image_2 = cv.LoadImageM(r"C:\Documents and Settings\rondou.chen\My Documents\Downloads\480_2.PNG")
dst = cv.CreateMat(image_1.rows, image_1.cols, cv.CV_8UC3)
cv.AddWeighted(image_1, alpha, image_2, beta, 0.0, dst)
#show
#cv.NamedWindow("mywin")
#cv.ShowImage("mywin", dst)
#cv.WaitKey(0)
cv.SaveImage(r"C:\Documents and Settings\rondou.chen\My Documents\Downloads\55555.png", dst)
