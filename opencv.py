import cv
import sys

##開圖
def amain():
    image = cv.LoadImage("C:\\Documents and Settings\\rondou.chen\\My Documents\\Downloads\\2_webp_ll.png")
    cv.NamedWindow("mywin")
    cv.ShowImage("mywin", image)
    cv.WaitKey(0)

##轉檔存檔
def convert(): 
    im = cv.LoadImageM(r"C:\Documents and Settings\rondou.chen\My Documents\Downloads\0000585255.jpg")
    print type(im)
    cv.SaveImage(r"C:\Documents and Settings\rondou.chen\My Documents\Downloads\54321.png", im)

##調整圖大小
def resize():
    original = cv.LoadImageM("C:\\Documents and Settings\\rondou.chen\\My Documents\\Downloads\\2_webp_ll.png")
    thumbnail = cv.CreateMat(original.rows / 10, original.cols / 10, cv.CV_8UC3)
    cv.Resize(original, thumbnail)
    cv.NamedWindow("mywin")
    cv.ShowImage("mywin", thumbnail)
    cv.WaitKey(0)

##截取圖片某一塊 crop
def get_sub_rect():
    img = cv.LoadImageM("C:\\Documents and Settings\\rondou.chen\\My Documents\\Downloads\\2_webp_ll.png")
    sub = cv.GetSubRect(img, (50, 0, 128, 256))
    cv.NamedWindow("mywin")
    cv.ShowImage("mywin", sub)
    cv.WaitKey(0)
    cv.SetZero(sub)

if __name__ == '__main__':
    resize()
