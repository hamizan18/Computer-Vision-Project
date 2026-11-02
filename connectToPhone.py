import cv2
import numpy as np

url = "http://154.14.224.165:8080/video"

cap = cv2.VideoCapture(url)
a=0

while True:
    a = a+1
    ret, frame = cap.read()

    if not ret:
        print("Gagal terhubung ke kamera HP.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_flip = cv2.flip(gray, 1)
    combined_window = np.hstack([gray, gray_flip])

    # frame.flip(1)
    frame = cv2.resize(frame, (640, 480))

    cv2.imshow("Kamera HP via OpenCV", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
print(a)

cap.release()
cv2.destroyAllWindows()
