import cv2

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

lowerGreen = (40, 50, 50)
upperGreen = (80, 255, 255)

lowerRed1 = (0, 120, 70)
upperRed1 = (10, 255, 255)

lowerRed2 = (170, 120, 70)
upperRed2 = (180, 255, 255)

while True:
    success, frame = camera.read()
    
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    maskGreen = cv2.inRange(hsv, lowerGreen, upperGreen)
    maskRed1 = cv2.inRange(hsv, lowerRed1, upperRed1)
    maskRed2 = cv2.inRange(hsv, lowerRed2, upperRed2)
    redMask = cv2.bitwise_or(maskRed1, maskRed2)
    
    cv2.imshow("Mask Red", redMask)
    cv2.imshow("Mask Green", maskGreen)
    greenPixels = cv2.countNonZero(maskGreen)
    redPixels = cv2.countNonZero(redMask)
    
    if redPixels > 500:
        cv2.putText(
            frame, # Frame tujuan
            "MiRAHH Lebih KEDETECT", # Teks yang munculs
            (20, 50), # Posisi Teks (x, y)
            cv2.FONT_HERSHEY_COMPLEX, # Font
            1, # Ukuran
            (0, 0, 255), # Warna Font
            2 # Ketebalan
        ) 
    elif greenPixels > 500:
        cv2.putText(
            frame,
            "iJOO Lebih KEDETECT",
            (20, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2
        )
    
    cv2.imshow("MIJAAN VISION", frame)
    
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()