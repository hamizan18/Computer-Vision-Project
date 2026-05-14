import cv2

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    success, frame = camera.read()
    frame = cv2.flip(frame, 1)
    
    if not success:
        break

    cv2.putText(
        frame, # Frame tujuan
        "COMPUTER VISION STARTED", # Teks yang munculs
        (20, 50), # Posisi Teks (x, y)
        cv2.FONT_HERSHEY_COMPLEX, # Font
        1, # Ukuran
        (0, 255, 0), # Warna Font
        2 # Ketebalan
    )
    
    cv2.imshow("MIJAAN VISION", frame)

    if cv2.waitKey(1) == ord('q'):
        break
    
    
camera.release()
cv2.destroyAllWindows()