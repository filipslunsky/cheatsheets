import cv2

image_name = "woman.jpg"

img = cv2.imread(image_name)
cv2.imshow('Test Image', img)
cv2.waitKey(10)
cv2.destroyAllWindows()

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# edges = cv2.Canny(img, 100, 200)
# cv2.imshow('Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# faces = face_cascade.detectMultiScale(gray)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

# cv2.imshow('Faces', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 5)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

#     cv2.imshow('Webcam Face Detection', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()