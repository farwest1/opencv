import cv2

# Lade das gewünschte Bild
img_path = 'lena'  # Ersetze durch den Pfad zu deinem Bild
img = cv2.imread(img_path)

# Lade den Haar-Klassifikator für Gesichter
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Konvertiere das Bild in Graustufen
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Suche nach Gesichtern
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# Zeichne Rechtecke um die erkannten Gesichter
for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
  roi = img[y:y+h, x:x+h]
  blurred_roi = cv2.blur(roi, (50, 50))
  img[y:y+h, x:x+w] = blurred_roi


# Zeige das Bild mit den markierten Gesichtern an
cv2.imshow('Gesichter erkannt', img)
cv2.waitKey(0)
cv2.destroyAllWindows()