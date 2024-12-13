import cv2 as cv

img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\WIN_20241206_16_07_26_Pro.jpg"

img=cv.imread(img_path)

cv.imshow("My_Image",img)

cv.waitKey(0)
cv.destroyAllWindows()