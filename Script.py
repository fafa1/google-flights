'''


Esse script faz requiscao do google fligts a cada 1h, usando o time.sleep(3600) e gera um arquivo txt, com todas as locucoes
ele rodou durante um dia e meio.
O que precisa agora e armazenar essas solutions em um banco de dados.
'''

import urllib
import urllib2
import json
import time

while 1:

 url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyA3758yM14aTX7aI9_v5AvKI2X1m56HszI" 

 code = {
 
  "request": {
    "passengers": {
      "adultCount": 1,
      "childCount": 1
    },
    "slice": [
      {
        "origin": "SSA",
        "destination": "NCE",
        "date": "2015-06-19",
        "permittedDepartureTime":
        {
          "kind": "qpxexpress#timeOfDayRange",
          "earliestTime": "22:00",
          "latestTime": "23:00"
        }
      },
      {
        "origin": "NCE",
        "destination": "SSA",
        "date": "2015-06-30",
        "permittedDepartureTime":
        {
          "kind": "qpxexpress#timeOfDayRange",
          "earliestTime": "05:00",
          "latestTime": "12:00"
        }
      }
    ],
    "solutions": 3
  }
}


 jsonreq = json.dumps(code, encoding = 'utf-8')
 req = urllib2.Request(url, jsonreq, {'Content-Type': 'application/json'})
 flight = urllib2.urlopen(req)
 response = flight.read()
 flight.close()
 #print(response)
 print("----------------")
 

 texto=(response)
 v_file= open("requests_60s(1).txt","a")
 conteudo=v_file.write(texto)
 v_file.close()

 time.sleep(3600)









