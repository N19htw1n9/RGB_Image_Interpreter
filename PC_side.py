import sys, os, json, time
sys.path.append(os.path.join(os.path.dirname(__file__),"httplib2/python2/"))

import httplib2
http = httplib2.Http()

if 1:
  url_json = 'http://10.0.0.241/jblink'   
  data = {'r': '50', 'g': '150', 'b': '255'}
  headers={'Content-Type': 'application/json; charset=UTF-8'}
  response, content = http.request(url_json, 'POST', headers=headers, body=json.dumps(data))
  print(response)
  print(content)