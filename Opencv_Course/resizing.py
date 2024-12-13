import cv2
img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\WIN_20241206_16_07_27_Pro.jpg"

img=cv2.imread(img_path)
cv2.imshow("image",img)

# resizing an image which is smaller than the original image

resized_small=cv2.resize(img,(640,480),interpolation=cv2.INTER_AREA)
cv2.imshow("resized small than the orginal",resized_small)


#without interpolation
resized_without_inter=cv2.resize(img,(640,480))
cv2.imshow("without interppolaton",resized_without_inter)


# resizing image to a larger than the original image


resized_large=cv2.resize(resized_without_inter,(1280,720),interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized large than the orginal",resized_large)



resized_large_without_inter=cv2.resize(resized_without_inter,(1280,720))
cv2.imshow("resized large than the orginal_without_inter",resized_large_without_inter)
cv2.waitKey(0)
cv2.destroyAllWindows()
