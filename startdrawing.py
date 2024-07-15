import cv2

img = cv2.imread('lena.jpg', 1)
height, width, channels = img.shape
print(height)
print(width)
print(channels)


img = cv2.arrowedLine(img, (0,0), (255,255), (0,0,255),2)
img = cv2.rectangle(img, (0,0), (100,100), 10,)

cv2.imshow('image', img)
k = cv2.waitKey(0)

cv2.destroyAllWindows()