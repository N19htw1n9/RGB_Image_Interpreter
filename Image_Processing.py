import cv2

path = 'butterfly.jpg'

img = cv2.imread(path, 1)

for k in range(0, img.shape):
  for i in range(0, img.shape[0]):
    pixel = img.item(k, i)
    print(pixel)