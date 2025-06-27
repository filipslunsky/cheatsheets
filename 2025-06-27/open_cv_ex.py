import cv2
import os

image_path = os.path.join(os.getcwd(), "woman.jpg")

image = cv2.imread(image_path)
if image is None:
    print("Image not found")
    exit()

cv2.imshow("Original Image", image)
cv2.waitKey(3000)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)

resized = cv2.resize(image, (300, 300))
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)

edges = cv2.Canny(image, threshold1=100, threshold2=200)
cv2.imshow("Edge Detection", edges)
cv2.waitKey(0)

image_with_rect = image.copy()
cv2.rectangle(image_with_rect, (50, 50), (250, 250), (0, 255, 0), 3)
cv2.imshow("Image with Rectangle", image_with_rect)
cv2.waitKey(1000)



cv2.imwrite("output_grayscale.jpg", gray)
cv2.imwrite("output_edges.jpg", edges)
print("Images saved to disk.")

cv2.destroyAllWindows()
