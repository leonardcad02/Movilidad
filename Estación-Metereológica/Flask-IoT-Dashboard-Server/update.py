import json, base64
import urllib.request
from random import choice
import time
import os
import requests


# method for enconde and decode data
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


# randlist = [i for i in range(20, 100,5)]

while 1:
    #Check the sensor data on the Wemos IP 
    response = requests.get('http://10.130.1.239:80')
    try:
        sensor_data = response.json()
        temperature = sensor_data['variables']['temperature']
        humidity = sensor_data['variables']['humidity']
        pollution = sensor_data['variables']['polution']
        uv = sensor_data['variables']['uv']
        noise = sensor_data['variables']['noise']
        #voltage = sensor_data['variables']['voltageStation']
        pmone = sensor_data['variables']['PM1']
        pmtwo = sensor_data['variables']['PM25']
        pmten = sensor_data['variables']['PM10']
        mydata = ['movilidad', 'MET12012', temperature, humidity, pollution, uv, noise, pmone, pmtwo, pmten]
        a = encode(mydata)
        url = 'http://127.0.0.1:5000/api/alshdlasdhlas/update/{}'.format(a)
        response = urllib.request.urlopen(url)
        print("[data]: "+ str(mydata))
        print("[Encoded Value]: "+ a)
        print("[url]: "+ url)
        html = response.read()
        print("[output]: " + str(html))
    except:
         print("Website Not online")
         time.sleep(2)
