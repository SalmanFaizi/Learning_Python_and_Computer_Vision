import cv2
img=cv2.imread(r"Opencv_Course\srk photo.jpg")

cv2.imshow("SRK Photo",img)

harcascade=cv2.CascadeClassifier("Opencv_Course\haarcascade_frontalface_default.xml")
detected_faces=harcascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=3)
print("faced detected",len(detected_faces))

for (x,y,w,h) in detected_faces:
    # x,y,w,h=detected_faces
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Detected Faces",img)
cv2.imwrite(r"Opencv_Course\Detected_Face.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()