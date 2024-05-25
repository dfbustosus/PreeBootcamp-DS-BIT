#python -m pip install -q opencv-python
import cv2
cap = cv2.VideoCapture('video_ejemplo.mp4')
# leer los frames del video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: # not False = True (solo chequear cuando no pueda leer mas frames)
        break

    # display el frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Desplegar el video y cerrarlo 
cap.release()
cv2.destroyAllWindows() # cuando se acabe el video se cierra