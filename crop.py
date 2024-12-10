import os
import cv2

image = cv2.imread(os.path.join('.', 'data', 'image-01.jpg'))

# Image shape is (height, width, num_of_channels)
print(image.shape)

cropped_image = image[300:440, 500:540] # 300:440 is the height interval and 500:540 is the width interval from where the crop is going to be applied

cv2.imshow('image', image)
cv2.imshow('cropped_image', cropped_image)
cv2.waitKey(0)