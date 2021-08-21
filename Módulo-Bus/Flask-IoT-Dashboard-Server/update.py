import json, base64
import urllib.request
from random import choice
import time
import os
import requests


def encode(data):
    data = json.dumps(data)
    message_bytes = data.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def decode(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return json.loads(message)

while 1:
    #Check the sensor data on the Wemos IP 
    response = requests.get('http://10.130.1.234:80')
    responseOne = requests.get('http://10.130.1.209:80')
    responseTwo = requests.get('http://10.130.1.222:80')
    responseThree = requests.get('http://10.130.1.231:80')
    #responseFour = requests.get('http://192.168.1.77:80')
    try:
        bus_data = response.json()
        personOne = responseOne.json()
        personTwo = responseTwo.json()
        personThree = responseThree.json()
        #personFour = responseFour()
        latitud = bus_data['variables']['latitud']
        longitud = bus_data['variables']['longitud']
        altitud = bus_data['variables']['altitud']
        speed = bus_data['variables']['velocidad']
        pone = personOne['variables']['person']        
        ptwo = personTwo['variables']['person']
        pthree = personThree['variables']['person']
        #pthree = 1
        #pfour = personFour['variables']['person']
        mydata = ['bus', 'BUS12012', latitud, longitud, altitud/1000, speed, pone, ptwo, pthree, 1]
        a = encode(mydata)
        url = 'http://127.0.0.1:5000/api/dfsdfsdfsfsdfcsd/update/{}'.format(a)
        response = urllib.request.urlopen(url)
        print("[data]: "+ str(mydata))
        print("[Encoded Value]: "+ a)
        print("[url]: "+ url)
        html = response.read()
        print("[output]: " + str(html))
        time.sleep(2)
    except:
         print("Website Not online")
         time.sleep(2)
