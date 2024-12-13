import cv2
video_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\WIN_20241206_16_04_02_Pro.mp4"


def frame_rescaling(frame,scaling_factor=0.5):
    frame_width=int(frame.shape[1])
    frame_height=int(frame.shape[0])
    dimensions=(frame_height,frame_width)
    frame_new=cv2.resize(frame,dimensions)

    return frame_new

# Rescaling Images

img=cv2.imread(r"C:\Users\salma\OneDrive\Pictures\Camera Roll\WIN_20241206_16_07_27_Pro.jpg")
img_resized=frame_rescaling(img)
cv2.imshow("Resized Image Window",img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rescaling video

capture=cv2.VideoCapture(0)

while True:
    is_true,frame=capture.read()

    if not is_true:
        print("All Frames Processed!!")
        break

    cv2.imshow("Reading_Video",frame)
    cv2.imshow("Reading_rescaled_Video",frame_rescaling(frame))

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()