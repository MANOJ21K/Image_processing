import cv2
import imutils
img=cv2.imread("Messi.jpg")


grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



img2=imutils.resize(img,width=500)



cv2.imwrite("GrayImage.jpeg",grayImg)




cv2.imshow("Oringinal",img)
cv2.imshow("ResizedImg",img2)
cv2.imshow("GrayImage",grayImg)    

