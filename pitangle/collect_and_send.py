#!/usr/bin/python
import Adafruit_DHT
import time
import json
from datetime import datetime
from datetime import datetime
from iota import Address, Iota, ProposedTransaction, TryteString

in_file = open("tangle/address_1.conf", "rb") # opening for [r]eading as [b]inary
ADDRESS = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

api = Iota("https://durian.iotasalad.org:14265")
receiver = Address(ADDRESS)

sensor = 11
pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    #print ('Temp: {0:0.1f} C  Humidity: {1:0.1f}'.format(temperature, humidity))
    measurment = {"humidity":humidity, "temperature":temperature,"measuredAt":str(datetime.now())}
    message = TryteString.from_string(json.dumps(measurment))
    tx = ProposedTransaction(address=receiver, value=0, message=message)
    api.send_transfer(depth=1, transfers=[tx])
    time.sleep(300)
