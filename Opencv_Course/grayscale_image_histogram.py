import cv2
import matplotlib.pyplot as plt
img_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\srk photo.jpg"
img=cv2.imread(img_path,0)
cv2.imshow("image",img)


hist=cv2.calcHist([img],[0],None,[256],[0,256])
cv2.imwrite(r"D:\Learning_Python\Opencv_Course\histogram_for_graysclae_image.jpg",hist)


plt.figure()
plt.title("Grayscale image histogram")
plt.xlabel("Bins")
plt.ylabel("Pixels")
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()