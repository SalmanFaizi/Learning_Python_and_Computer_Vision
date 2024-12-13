import cv2
def change_res(width,height):
    capture.set(3,width)
    capture.set(4,height)


video_path="C:\Users\salma\OneDrive\Pictures\Camera Roll\WIN_20241206_16_04_02_Pro.mp4"
capture=cv2.VideoCapture(video_path)

while True:
    is_true,frame=capture.read()

    if not is_true:
        print("All Frames Processed!!")
        break

    # cv2.imshow("Reading_Video",frame)
    cv2.imshow("Reading_rescaled_Video",change_res(frame.shape[1],frame.shape[0]))

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()