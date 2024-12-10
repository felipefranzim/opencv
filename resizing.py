import os
import cv2

image = cv2.imread(os.path.join('.', 'data', 'image-01.jpg'))

# Image shape is (height, width, num_of_channels)
print(image.shape)

new_width = int(image.shape[1] / 2)
new_height = int(image.shape[0] / 2)
print(f"{new_width} x {new_height}")

resized_image = cv2.resize(image, (new_width, new_height))
print(resized_image.shape)

cv2.imshow('image', image)
cv2.imshow('resized_image', resized_image)
cv2.waitKey(0)