import cv2
img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\srk photo.jpg"
import numpy as np

img=cv2.imread(img_path)
cv2.imshow("Image",img)

# Grayscaling the image

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)


# apply blurring

blur=cv2.GaussianBlur(gray,(1,1),1.0)
cv2.imshow("Blur",blur)

# canny edge detection

edges=cv2.Canny(blur,125,150,)
cv2.imshow("Edges",edges)

#binarizing an image

# binary_img=cv2.threshold(img,125,150,cv2.THRESH_BINARY)
ret,thresh=cv2.threshold(gray,120,150,cv2.THRESH_BINARY)
cv2.imshow("binary image",thresh)

# finding contours.

contours,hir=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print(len(contours))

# empty image

empty_img=np.zeros(img.shape,dtype='uint8')
cv2.imshow("empty image",empty_img)

# draw contours

contours_drawing=cv2.drawContours(empty_img,contours=contours,contourIdx=-1,color=(0,255,0),thickness=1)
cv2.imshow("controus drawing",contours_drawing)
cv2.waitKey(0)
cv2.destroyAllWindows()
