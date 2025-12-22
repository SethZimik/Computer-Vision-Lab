import cv2

# IMAGE READING & DISPLAY

img_color = cv2.imread("sample.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread("sample.jpg", cv2.IMREAD_UNCHANGED)

cv2.imshow("Color Image", img_color)
cv2.imshow("Grayscale Image", img_gray)
cv2.imshow("Unchanged Image", img_unchanged)

cv2.waitKey(0)
cv2.destroyAllWindows()


# VIDEO CAPTURE & STORAGE

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not accessible")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output_video.mp4", fourcc, 20.0, (640, 480))

print("Press 'q' to stop video recording")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow("Live Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
