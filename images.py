import os
import cv2

# Read an image
image_path = os.path.join('.', 'data', 'image-01.jpg')
img = cv2.imread(image_path)

# Write image in disc

cv2.imwrite(os.path.join('.', 'data', 'image-01_out.jpg'), img)

# Visualize image
cv2.imshow('image', img)
cv2.waitKey(0)