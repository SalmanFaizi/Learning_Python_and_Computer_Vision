import cv2
img_path=r"Opencv_Course\cat.webp"
img=cv2.imread(img_path)
cv2.imshow("Cat",img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

thresold,thresh=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
cv2.imshow("Thresold",thresh)

thresold,thresh_inv=cv2.threshold(gray,125,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresold_inv",thresh_inv)

thresh_adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow("Adaptive thresolding",thresh_adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()

