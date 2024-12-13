import cv2

video_path=r"C:\Users\salma\OneDrive\Pictures\Camera Roll\WIN_20241206_16_04_02_Pro.mp4"

capture=cv2.VideoCapture(video_path)

while True:
    is_true,frame=capture.read()

    if not is_true:
        print("All Frames Processed!!")
        break

    cv2.imshow("Reading_Video",frame)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()