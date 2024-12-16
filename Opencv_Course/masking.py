import cv2
import numpy as np

img=cv2.imread(r"C:\Users\salma\OneDrive\Pictures\Camera Roll\only_face.jpg")
cv2.imshow("Image",img)

blank_img=np.zeros((img.shape[:2]),dtype='uint8')
cv2.imshow("blank image",blank_img)

# rectangle=cv2.rectangle(blank_img.copy(),(50,50),(350,350),(255,255,255),-1)
# cv2.imshow("rectangle",rectangle)
circle=cv2.circle(blank_img.copy(),(200,200),200,(255,255,0),-1)
cv2.imshow("circle",circle)

mask=cv2.bitwise_and(img,img,mask=circle)
cv2.imshow("Making",mask)

cv2.waitKey(0)

cv2.destroyAllWindows()