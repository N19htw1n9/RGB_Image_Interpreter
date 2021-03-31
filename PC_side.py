#Get the function used for image processing
from Image_Processing import freqPixelRGB

import sys, os, json, time

sys.path.append(os.path.join(os.path.dirname(__file__),"httplib2/python2/"))
#library for HTTP requsts
import httplib2

http = httplib2.Http()
#prompt user for the image name
filename = input("Enter the name of the image (if it is in the same folder) or a path to it: ")
#common_colors is now an array of five tripes with rgb values
common_colors = freqPixelRGB(filename)
url_json = 'http://10.0.0.241/jblink'   
headers={'Content-Type': 'application/json; charset=UTF-8'}
for x in common_colors:
#create a dictionary with a color
  data = {
    "r": x[0],
    "g": x[1],
    "b": x[2] 
  }
  print(json.dumps(data))
  #make a request that sends json data to the ESP
  response, content = http.request(url_json, 'POST', headers=headers, body=json.dumps(data))
  print(response)
  print(content)
  #a small delay to let ESP process the data
  time.sleep(1)

if 0:
  url_json = 'http://10.0.0.241/jblink'   
  data = {'r': '0', 'g': '0', 'b': '100'}
  headers={'Content-Type': 'application/json; charset=UTF-8'}
  response, content = http.request(url_json, 'POST', headers=headers, body=json.dumps(data))
  print(response)
  print(content)