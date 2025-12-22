import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
    exit()

# Get image dimensions
height, width = img.shape[:2]


# 1. SCALING
scaled_img = cv2.resize(img, None, fx=0.5, fy=0.5)


# 2. TRANSLATION
tx, ty = 100, 50   # shift right by 100, down by 50
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated_img = cv2.warpAffine(img, translation_matrix, (width, height))

# 3. ROTATION
angle = 45
rotation_matrix = cv2.getRotationMatrix2D((width // 2, height // 2), angle, 1)
rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

# DISPLAY RESULTS
cv2.imshow("Original Image", img)
cv2.imshow("Scaled Image", scaled_img)
cv2.imshow("Translated Image", translated_img)
cv2.imshow("Rotated Image", rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
