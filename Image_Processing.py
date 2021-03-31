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

'''
Processes image and returns the
5 most frequently occurring RGB values
'''
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
    maxVal = max(freqList, key = freqList.get)
    if (establishThreshold(valList, maxVal) == True
        and isGrayOrBlack(maxVal) == False):
      valList.append(maxVal)
      del freqList[maxVal]
      count += 1
    
    else:
      del freqList[maxVal]
  
  return valList

'''
Checks each element of the list and compares
to a set of RGB values. Returns true if it follows
the 10% variance methodology and false otherwise
'''
def establishThreshold(li, val):
  ret = True
  
  if len(li) == 0:
    return True
  
  for k in li:
    if checkVariance(k, val) == False:
      ret = False
  
  return ret

'''
Compares two sets of RGB values and returns
True if their variance is equal to or greater
than 10% higher OR equal to or less than 10% lower
'''
def checkVariance(val1, val2):
  if ((int(val1[0] * 0.9) >= val2[0])
      and (int(val1[1] * 0.9) >= val2[1])
      and (int(val1[2] * 0.9) >= val2[2])):
    return True
  
  elif ((int(val1[0] * 1.1) <= val2[0])
      and (int(val1[1] * 1.1) <= val2[1])
      and (int(val1[2] * 1.1) <= val2[2])):
    return True
  
  return False

def isGrayOrBlack(val):
  if (val[0] == val[1] and val[1] == val[2]):
    return True
  elif (abs(val[0] - val[1]) <= 16 and val[1] == val[2]):
    return True
  elif (val[0] == val[1] and abs(val[1] - val[2]) <= 16 ):
    return True
  elif (val[0] == val[2] and abs(val[2] - val[1]) <= 16 ):
    return True
  
  return False

# For testing
print(freqPixelRGB('butterfly.jpg'))