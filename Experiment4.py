import cv2

# Read the image
img = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found")
    exit()

# Apply Canny Edge Detection
# 100 = lower threshold, 200 = upper threshold
edges = cv2.Canny(img, 100, 200)

# Display original and edge-detected images
cv2.imshow("Original Image", img)
cv2.imshow("Edge Detected Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
