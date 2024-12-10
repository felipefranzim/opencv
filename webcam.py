import cv2

# Read webcam
webcam = cv2.VideoCapture(0) # 0 is de index os the attatched webcam in the computer

# Read frames from webcam

while True:
    ret, frame = webcam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): # Will wait 40 milleseconds AND if the user press the letter Q on keyboard, it'll break the loop
        break

# Release memory
webcam.release()
cv2.destroyAllWindows()