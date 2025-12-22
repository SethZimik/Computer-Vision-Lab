import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image in grayscale
img = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found")
    exit()

# 1. Compute Histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot original histogram
plt.figure()
plt.title("Original Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# 2. Histogram Equalization
equalized_img = cv2.equalizeHist(img)

# Compute histogram of equalized image
hist_eq = cv2.calcHist([equalized_img], [0], None, [256], [0, 256])

# Plot equalized histogram
plt.figure()
plt.title("Equalized Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(hist_eq)
plt.xlim([0, 256])
plt.show()

# Display original and equalized images
cv2.imshow("Original Image", img)
cv2.imshow("Equalized Image", equalized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
