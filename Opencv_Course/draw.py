import cv2
import numpy as np
img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\WIN_20241206_16_07_27_Pro.jpg"
#Reading an image
img=cv2.imread(img_path)
# cv2.imshow("Image",img)
# cv2.waitKey(0)

#Creating a blank image
blank_image=np.zeros((500,500,3),dtype='uint8')
cv2.imshow("blank",blank_image)

# #Changing color of the some parts of the blank image
# blank_image[0:100,:100,:3]=(0,255,0)
# cv2.imshow("blank color change",img)

# #Changing color of the some parts of the  image
# img[0:100,:100,:3]=(0,255,0)
# cv2.imshow("blank color change",img)

# #Drawing a line on the blank image
# cv2.line(blank_image,(0,255),(255,255),(0,255,0),thickness=3)
# cv2.imshow('line showing',blank_image)


# #Drawing a rectangle on the blank image
# cv2.rectangle(blank_image,(0,0),(255,255),color=(255,255,0),thickness=-1)
# cv2.imshow('rectangle showing',blank_image)


# #Drawing a circle on the blank image
# cv2.circle(blank_image,center=(255,255),radius=15,color=(255,0,0),thickness=-1)
# cv2.imshow('rectangle showing',blank_image)

# #Putting text on the image

# cv2.putText(img,text="hello salman",org=(0,0),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=2.0,color=(255,255,255),thickness=3)
# cv2.imshow("put text on the image",img)



#Putting text on the image in middle

height_img=img.shape[0]
width_img=img.shape[1]
center=(width_img//2,height_img//2)
print(f'height {height_img} width {width_img} and center is {center}')
cv2.putText(img,text="hello salman",org=center,fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1.0,color=(0,255,255),thickness=2)
cv2.imshow("put text on the image",img)

# Cropping image

img_crop=img[0:720,0:800]
cv2.imshow("crop image",img_crop)


cv2.waitKey(0)
cv2.destroyAllWindows()