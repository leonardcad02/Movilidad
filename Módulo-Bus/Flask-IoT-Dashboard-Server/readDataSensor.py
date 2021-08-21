# Importamos paquetes que necesitamos
import os
import requests
import time
import datetime

# Consulta los datos del sensor en la IP del Wemos
response = requests.get('http://192.168.1.78:80')


# Setup del timestamp 
t = time.time()
#timegood = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

# Convierte la respuesta del servidor web en un diccionario de Python

def readData():       
       sensor_data = response.json()
       temperature = sensor_data['variables']['temperature']
       humidity = sensor_data['variables']['humidity']
       pollution = sensor_data['variables']['polution']
       uv = sensor_data['variables']['uv']
       noise = sensor_data['variables']['noise']
       voltage = sensor_data['variables']['voltageStation']
       pmone = sensor_data['variables']['PM1']
       pmtwo = sensor_data['variables']['PM25']
       pmten = sensor_data['variables']['PM10']
       return temperature,humidity,pollution,uv,noise,pmone,pmtwo,pmten

readData()

