import os
import cv2

# Read video
video_path = os.path.join('.', 'data', 'video.mp4')
video = cv2.VideoCapture(video_path)

# Visual video
ret = True
while ret:
    ret, frame = video.read() # ret is a bool that indicates if the frame was successfully captured or not. So, then there's no more frames to get, the ret is false
    
    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40) # Wait 40 milleseconds

# Release memory
video.release()
cv2.destroyAllWindows()