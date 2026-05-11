import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    
    cv2.putText(frame, 'Smart Attendance System', (50,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow('Attendance', frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
