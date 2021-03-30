'''

First install Pillow:
> (sudo) pip3 install pillow

You may/may not also need to install wheel
> pip install wheel

Python program for reading in pixels from image, and returning
the 5 most recurring RGB values in the image

Inspiration was taken from:
https://predictivehacks.com/iterate-over-image-pixels/
https://pillow.readthedocs.io/en/stable/reference/Image.html
'''

import PIL
from PIL import Image

def freqPixelRGB(path):
  
  img = Image.open(path)

  freqList = {}
  for x in range(img.width):
    for y in range(img.height):
      item = img.getpixel((x, y))
      if item in freqList:
        freqList[item] += 1
      else:
        freqList[item] = 1

  count = 0
  valList = []
  while count < 5:
    maxKey = max(freqList, key = freqList.get)
    valList.append(maxKey)
    del freqList[maxKey]
    count += 1
  
  return valList

# For testing
# print(freqPixelRGB('butterfly.jpg'))