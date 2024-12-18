import cv2
import numpy
import matplotlib.pyplot as plt
img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\srk photo.jpg"

img=cv2.imread(img_path)
cv2.imshow("Image",img)


plt.figure()
plt.title("Histogram for rgb image")
plt.xlabel("Bins")
plt.ylabel("Pixels")


colors=('b','g','r')
for i , col in enumerate(colors):
    hist=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv2.imwrite(r"D:\Learning_Python\Opencv_Course\histogram_for_rgb_image.jpg",hist)


cv2.waitKey(0)
cv2.destroyAllWindows()