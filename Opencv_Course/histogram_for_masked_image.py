import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\srk photo.jpg"
img=cv2.imread(img_path,0)
cv2.imshow("image",img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow("blank image",blank)

circle=cv2.circle(blank,(img.shape[1]//2,img.shape[0]//2),50,(255,255,255),-1)
cv2.imshow("circle",circle)

mask=cv2.bitwise_and(circle,img)
cv2.imshow("mask",mask)

hist=cv2.calcHist([img],[0],mask,[256],[0,256])
cv2.imwrite(r"D:\Learning_Python\Opencv_Course\histogram_for_masked_image.jpg",hist)


plt.figure()
plt.title("Grayscale image histogram")
plt.xlabel("Bins")
plt.ylabel("Pixels")
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()