success, frame = camrea.read()
success -> berhasil baca atau tidak
fram -> gambar dari kamera

if cv2.waitKey(1) == 27:
27 = tombol ESC
pake ord('button_here') kalo mau pake tombol selain ESQ

frame = cv2.flip(frame, 1) ubah gini biar gaa mirror di Windows

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW) ini fungsinya biar lebih cepat munculnya

