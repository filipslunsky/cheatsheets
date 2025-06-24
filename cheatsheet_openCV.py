# Import knihovny
import cv2

# Načítání a ukládání obrázků
img = cv2.imread("obrazek.jpg")              # načte obrázek (v barvách BGR)
cv2.imwrite("vystup.jpg", img)               # uloží obrázek do souboru

# Zobrazení obrázku v okně
cv2.imshow("Okno", img)                      # zobrazí obrázek v okně
cv2.waitKey(0)                               # čeká na stisk klávesy
cv2.destroyAllWindows()                      # zavře všechna okna

# Změna velikosti / škálování
resized = cv2.resize(img, (640, 480))        # změní velikost na přesné rozměry
resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # změna velikosti podle poměru

# Ořez obrázku (crop)
cropped = img[100:400, 200:500]              # ořez na oblast [y1:y2, x1:x2]

# Převod barev
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       # převod na černobílý (grayscale)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)         # převod na RGB (např. pro matplotlib)

# Filtry a úpravy
blurred = cv2.GaussianBlur(img, (5, 5), 0)         # rozmazání
edges = cv2.Canny(img, 100, 200)                   # detekce hran (Canny edge)

# Kreslení na obrázek
cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # nakreslí obdélník
cv2.circle(img, (x, y), radius=50, color=(255,0,0), thickness=3)  # kruh
cv2.putText(img, "Text", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)  # text

# Detekce obličejů (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Práce s kamerou (webcam)
cap = cv2.VideoCapture(0)                     # otevře defaultní kameru

while True:
    ret, frame = cap.read()
    cv2.imshow("Live", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):     # ukončení po stisknutí Q
        break

cap.release()
cv2.destroyAllWindows()

# Získání informací o obrázku
img.shape    # (výška, šířka, počet kanálů) např. (480, 640, 3)
img.dtype    # datový typ pixelů (např. uint8)
