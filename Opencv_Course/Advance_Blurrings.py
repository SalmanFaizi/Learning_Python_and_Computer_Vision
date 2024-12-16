import cv2
img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\srk photo.jpg"
img=cv2.imread(img_path)
cv2.imshow("Image",img)


# Average or normal blurring
# this blur is just like average pooling in cnn just calculates the average pixel value 

avg_blur=cv2.blur(img,(3,3))
cv2.imshow("AVG_BLUR",avg_blur)

# Gausian blur 
# this blurring technique tends to assign weight to each pixel and calculate their avg of multiples 

Gaussin_blur=cv2.GaussianBlur(img,(3,3),1)
cv2.imshow("Gaussin blur",Gaussin_blur)

# Median Blur 

Median_blue=cv2.medianBlur(img,3)
cv2.imshow("Median blur",Median_blue)


# bilateral blurring

bilateral_blur=cv2.bilateralFilter(img,70,30,30)
cv2.imshow("Bilateral Image",bilateral_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()