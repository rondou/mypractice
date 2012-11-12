import cv2
import sys
from cv2 import cv
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

##模糊化
def Gaussian_Blur():
    image_1 = cv.LoadImageM(r"C:\Documents and Settings\rondou.chen\My Documents\Downloads\480_1.PNG")
    dst = cv.CreateMat(image_1.rows, image_1.cols, cv.CV_8UC3)
    cv2.GaussianBlur(image_1,(3,3),dst)
    cv.NamedWindow("mywin")
    cv.ShowImage("mywin", dst)
    cv.WaitKey(0)
##銳利
def sharpen():
    image_1 = cv.LoadImageM(r"C:\Documents and Settings\rondou.chen\My Documents\Downloads\snapshot5.png",0)
    imwidth = image_1.rows
    imheight = image_1.cols
##    #dst = cv.CreateMat(image_1.rows, image_1.cols, cv.CV_32FC1)
    dst = cv.CreateImage((imheight,imwidth), 32, 1)
##    dst = cv.CreateMat(image_1.rows, image_1.cols, cv.CV_8UC1)
##    dst = cv.CreateImage(cv.GetSize(imheight,imwidth), 32, 1)
    for r in xrange(image_1.rows):
        for c in xrange(image_1.cols):
            dst[r, c] = image_1[r, c]
    lapl = cv.CreateImage((imheight,imwidth,),32,1)
    m = cv.CreateMat(3, 3, cv.CV_8UC1)
    m[0, 0] = -1
    m[0, 1] = -1
    m[0, 2] = -1
    m[2, 0] = -1
    m[2, 1] = -1
    m[2, 2] = -1
    m[1, 0] = -1
    m[1, 2] = -1
    m[1, 1] = 9
    cv.Filter2D(dst,lapl,m)
    maxv = 0
    for r in xrange(image_1.rows):
        for c in xrange(image_1.cols):
            if(lapl[r, c] > maxv):
                maxv = lapl[r, c]
    for r in xrange(image_1.rows):
        for c in xrange(image_1.cols):
            v = int(255 * lapl[r, c] / maxv) if maxv > 0 else v
            image_1[r, c] = image_1[r, c] + v
    maxv = 0
    for r in xrange(image_1.rows):
        for c in xrange(image_1.cols):
            if(image_1[r, c] > maxv):
                maxv = image_1[r, c]
    for r in xrange(image_1.rows):
        for c in xrange(image_1.cols):
            v = int(255 * image_1[r, c] / maxv)
            image_1[r, c] = v
                
    cv.NamedWindow("mywin")
    cv.ShowImage("mywin", image_1)
    cv.WaitKey(0)
##灰階
def gary():
    image_1 = cv.LoadImageM(r"C:\Documents and Settings\rondou.chen\My Documents\Downloads\2_webp_ll.jpg",0)
    imwidth = image_1.rows
    imheight = image_1.cols
    # convert to 32 bit
##    #dst = cv.CreateMat(image_1.rows, image_1.cols, cv.CV_32FC1)
    dst = cv.CreateImage((imheight,imwidth), 32, 1)
##    dst = cv.CreateMat(image_1.rows, image_1.cols, cv.CV_8UC1)
##    dst = cv.CreateImage(cv.GetSize(imheight,imwidth), 32, 1)
##    print dst
##    for r in xrange(dst.height):
##        print r
    print image_1
##    print dst
    print image_1[0, 1]
    for r in xrange(image_1.rows):
        for c in xrange(image_1.cols):
            dst[r, c] = image_1[r, c]
    cv.NamedWindow("mywin")
    cv.ShowImage("mywin", dst)
    cv.WaitKey(0)
def test_creat_image():
    im = cv.LoadImageM(r"C:\Documents and Settings\rondou.chen\My Documents\Downloads\2_webp_ll.jpg", 1)
    dst = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_16S, 3)
    cv.NamedWindow("mywin")
    cv.ShowImage("mywin", dst)
    cv.WaitKey(0)
if __name__ == '__main__':
    sharpen()
