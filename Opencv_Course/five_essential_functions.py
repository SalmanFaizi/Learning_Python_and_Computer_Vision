import cv2
img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\WIN_20241206_16_07_27_Pro.jpg"
img=cv2.imread(img_path)
img=cv2.resize(img,(640,480))
cv2.imshow("image",img)

# grayscale the image

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("image_gray",gray)


# Blur the image

blur=cv2.GaussianBlur(img,(9,9),1.0)
cv2.imshow("imageblur",blur)


# Edge cascade
edge=cv2.Canny(blur,110,150)
cv2.imshow("canny edge",edge)

# dialation 
dilate=cv2.dilate(edge,(5,5),iterations=5)
cv2.imshow("Dialted image",dilate)

# Eroding 
erode=cv2.erode(dilate,(5,5),iterations=5)
cv2.imshow("Eroding ",erode)
cv2.waitKey(0)
