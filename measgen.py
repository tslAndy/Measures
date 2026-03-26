import math
import random
import time
import requests

tiedosto = open("mittaukset.txt", "w")

i = 0
while i < 100:
    measurement = {}
    measurement["time"] = i 
    measurement["pressure"] = math.sin(i/10) + (random.random() * 2 - 1)
    measurement["temperature"] = math.cos(i/15) + (random.random() * 4 - 2)
    measurement["humidity"] = math.sin(i/20) + (random.random() * 6 - 3)

    response =  requests.post('http://localhost:5000/api/measurements', json=measurement)
    if response.status_code == 200:
        print("Datan lähetys onnistui")
    else: 
        print("Lähetys ei onnistunut")

    time.sleep(1)
    i += 1

    # measurement = {}
    # measurement["api_key"] = "EQ4VDIN8YLZHA5KB"
    # measurement["field1"] = math.sin(i/10) + (random.random() * 2 - 1)
    # measurement["field2"] = math.cos(i/15) + (random.random() * 4 - 2)
    # measurement["field3"] = math.sin(i/20) + (random.random() * 6 - 3)

    # s = str(measurement["api_key"]) + " " + str(measurement["field1"]) + " " + str(measurement["field2"]) + " " + str(measurement["field3"])
    # tiedosto.write(s + "\n")
    
    # response = requests.post('https://api.thingspeak.com/update.json', json=measurement)
    
    # if response.status_code == 200:
    #     print("Datan lähetys onnistui")
    # else: 
    #     print("Lähetys ei onnistunut")

    # time.sleep(1)
    # i += 1

tiedosto.close()
