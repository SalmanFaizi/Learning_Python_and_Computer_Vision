import cv2
img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\srk photo.jpg"

img=cv2.imread(img_path)
cv2.imshow("img",img)

# BGR to GrayScale

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

# BGR  to HSV

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)

# bgr to lab

lab=cv2.cvtColor(img,cv2.COLOR_BGR2Lab)
cv2.imshow('Lab',lab)

# BGR to RGB

rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("rgb",rgb)



# Reverse transformations

# RGB to BGR 

rgb_to_bgr=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR)
cv2.imshow("RGB--->BGR",rgb_to_bgr)

# HSV to RGB
hsv_to_bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow("HSV--->BGR",hsv_to_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
