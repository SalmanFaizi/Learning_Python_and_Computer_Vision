import cv2
import numpy as np

blank_img=np.zeros((400,400),dtype='uint8')
cv2.imshow("blank image",blank_img)

rectangle=cv2.rectangle(blank_img.copy(),(50,50),(350,350),(255,255,255),-1)
cv2.imshow("rectangle",rectangle)
circle=cv2.circle(blank_img.copy(),(200,200),200,(255,255,0),-1)
cv2.circle(blank_img,(200,200),50,(0,255,0),-1)
cv2.imshow("circle",circle)

# Bitwise operations

# bitwise and operation
bitwise_and=cv2.bitwise_and(rectangle,circle)
cv2.imshow("bitwise and ",bitwise_and)

# bitwise or operation

bitwise_or=cv2.bitwise_or(rectangle,circle)
cv2.imshow("bitwise_or",bitwise_or)

# bitwise xor operation

bitwise_xor=cv2.bitwise_xor(rectangle,circle)
cv2.imshow("bitwise_xor",bitwise_xor)

# bitwise not operation

bitwise_not=cv2.bitwise_not(circle.copy())
cv2.imshow("bitwise_not",bitwise_not)
cv2.waitKey(0)

cv2.destroyAllWindows()