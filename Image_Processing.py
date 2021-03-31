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

1. Creates a frequency list of RGB values
2. Finds the maximum frequency
'''
def freqPixelRGB(path):
  
  img = Image.open(path)

  freqList = {}
  for x in range(img.width):
    for y in range(img.height):
      item = img.getpixel((x, y))
      # Creates a frequency list of RGB values
      if item in freqList:
        freqList[item] += 1
      else:
        freqList[item] = 1

  count = 0
  valList = []
  while count < 5:
    # Finds the maximum occurrence of a particular RGB value
    maxVal = max(freqList, key = freqList.get)
    # Checks to see if the value is within threshold and excludes dark colors
    if (establishThreshold(valList, maxVal) == True
        and isDark(maxVal) == False):
      valList.append(maxVal)
      del freqList[maxVal]
      count += 1
    
    # If value isn't within the threshold or is black or gray,
    # the value will be deleted from the frequency list
    # to prepare for the next iteration
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
True if their variance is greater than 10% lower
OR less than 10% higher
'''
def checkVariance(val1, val2):
  if ((int(val1[0] * 0.9) > val2[0])
      and (int(val1[1] * 0.9) > val2[1])
      and (int(val1[2] * 0.9) > val2[2])):
    return True
  
  elif ((int(val1[0] * 1.1) < val2[0])
      and (int(val1[1] * 1.1) < val2[1])
      and (int(val1[2] * 1.1) < val2[2])):
    return True
  
  return False

'''
Checks to see if the provided
RGB value is a dark color (which couldn't
be displayed on the Arduino LED)
'''
def isDark(val):
  # Neutral gray colors contain the same 3 values
  if (val[0] == val[1] and val[1] == val[2]):
    return True
  # Removing darker shades from the set
  elif (val[0] == 0 and val[1] == 0
        and val[2] < 100):
    return True
  elif (val[0] == 0 and val[2] == 0
        and val[1] < 100):
    return True
  elif (val[1] == 0 and val[2] == 0
        and val[0] < 100):
    return True
  elif (abs(val[0] - val[1]) <= 16 and abs(val[1] == val[2]) <= 16
        and abs(val[0] == val[2]) <= 16):
    return True
  
  return False

# For testing
print(freqPixelRGB('butterfly.jpg'))