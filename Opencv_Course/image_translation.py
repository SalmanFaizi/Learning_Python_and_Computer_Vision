import cv2
import numpy as np 

img_path=r"C:\Users\salma\Downloads\face detection 2.png"
img=cv2.imread(img_path)
print("image",img)
cv2.imshow("image",img)


def translation_fn(img,x,y):
    matrix=np.float32([[1,0,x],[0,1,y]])
    # print(matrix)
    dimensions=(img.shape[1],img.shape[0])
    transformed_img=cv2.warpAffine(img,matrix,dimensions)
    print("transformed image",transformed_img)
    return transformed_img


# x--> right
# y--> Down
# -x--> left
# -y--> up
new_img=translation_fn(img,100,100)
cv2.imshow("translated image",new_img)



def img_rotation(img,angle,rootPoint=None):
    (height,width)=img.shape[:2]
    
    if rootPoint is None:
        rootPoint=(width//2,height//2)
        
    rootmat=cv2.getRotationMatrix2D(rootPoint,angle,1.0)
    dimensions=(img.shape[0],img.shape[1])
    return cv2.warpAffine(img,rootmat,dimensions)

# Rotation of the image in clock wise direction then give negative values else positive.
img_rotated=img_rotation(img,-45)
cv2.imshow("rotated_img",img_rotated)

# Flipping the image
# Flippping code 0 flips by vertical direction and 1 flips by horizontal direction and -1 flips in both the directions
flip=cv2.flip(img,0)

cv2.imshow("Flip img",flip)
cv2.waitKey(0)
cv2.destroyAllWindows()