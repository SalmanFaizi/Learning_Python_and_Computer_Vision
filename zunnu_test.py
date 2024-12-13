import cv2
import numpy as np
# import numpy as np# black_img = np.array([[[0,0,0],[0,0,0],[0,0,0]]])
# # img = cv2.imread(r"C:\Users\salma\OneDrive\Pictures\Camera Roll\WIN_20241206_16_04_08_Pro.jpg")
# # print(img)
# import cv2
# import numpy as np

# create a black image
# display the image using opencv
black_img = np.zeros((380,740,3))
black_img= cv2.line()
cv2.imshow('black image', black_img)
cv2.waitKey(0)
# print("height",img.shape[0])
# print("width",img.shape[1])

# grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# reimg = cv2.resize(img, (720,480))
# cv2.imshow("img",img)
# print("height",reimg.shape[0])
# print("width",reimg.shape[1])
# cv2.waitKey(0)
cv2.destroyAllWindows()


# # video_path=
# capture=cv2.VideoCapture(0)
# while True:
#     is_true,frame=capture.read()

#     if is_true is None:
#         print("Empty frame received so exiting...")
#         break
#     cv2.imshow("Reading Video",frame)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

# capture.release()
# cv2.destroyAllWindows()























# capture = cv2.VideoCapture(0)

# while True:
#     is_true, frame = capture.read(1)

#     if is_true is None:
#         print("video is not reading... ")
#         break
#     flip_img = cv2.flip(frame, 1)
#     print(flip_img.shape)
#     # cv2.putText(flip_img, "zunnu",(480//2,640//2),2,3.14, 2, 3)
#     # cv2.circle(flip_img,(640//2,480//2), 10, (255,255,255), 3)
#     cv2.imshow("video reading", flip_img)
#     if cv2.waitKey(1) & 0xFF == ord("z"):
#         break

# capture.release()
# cv2.destroyAllWindows()
# import numpy as np
# black_img = np.zeros((380,740,3))
# cv2.imshow(black_img)
# print(black_img)