import cv2
import numpy as np
img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\srk photo.jpg"

img=cv2.imread(img_path)
cv2.imshow("image",img)

blank_img=np.zeros(img.shape[:2],dtype="uint8")
cv2.imshow("blank image",blank_img)


b,g,r=cv2.split(img)

cv2.imshow("Blue",b)
cv2.imshow("greeen",g)
cv2.imshow("red",r)


merged_img=cv2.merge([b,g,r])
cv2.imshow("Merged Image",merged_img)


Blue=cv2.merge([b,blank_img,blank_img])

cv2.imshow("Blue_merged",Blue)

Green=cv2.merge([blank_img,g,blank_img])
cv2.imshow("greeen_merged",Green)


red=cv2.merge([blank_img,blank_img,r])
cv2.imshow("red_merged",red)

cv2.waitKey(0)
cv2.destroyAllWindows()