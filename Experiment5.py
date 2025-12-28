import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
    exit()


# 1. Smoothing (Blurring)

# Using Gaussian Blur
smoothed_img = cv2.GaussianBlur(img, (7,7), 0)


# 2. Sharpening
# Create a sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
sharpened_img = cv2.filter2D(img, -1, kernel)


# Display Results
cv2.imshow("Original Image", img)
cv2.imshow("Smoothed Image", smoothed_img)
cv2.imshow("Sharpened Image", sharpened_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

