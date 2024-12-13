import cv2

capture=cv2.VideoCapture(0)

while True:
    is_true,frame=capture.read()

    if not is_true:
        print("All Frames Processed!!")
        break

    frame=cv2.flip(frame,1)

    cv2.imshow("Reading_Video",frame)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()