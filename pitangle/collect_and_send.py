#!/usr/bin/python
import Adafruit_DHT
import time
import json
import sys
from datetime import datetime
from datetime import datetime
from iota import Address, Iota, ProposedTransaction, TryteString

#read the file from the seed file (also change the value of the seed file locally)
seed_file = open("tangle/config/seed.conf", "rb") # opening for [r]eading as [b]inary
seed = seed_file.read() # if you only wanted to read 512 bytes, do .read(512)
seed_file.close()
address_file = open("tangle/config/address_pi.conf", "rb") # opening for [r]eading as [b]inary
ADDRESS = address_file.read() # if you only wanted to read 512 bytes, do .read(512)
address_file.close()

api = Iota("https://durian.iotasalad.org:14265", seed)
receiver = Address(ADDRESS)

sensor = 11
pin = 4

time_to_sleep = 300

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    timestamp = datetime.now()
    print('Took reading at {0:s}. Now sending. Temperature: {1:0.1f} C, humidity: {2:0.1f}%.'.format(timestamp.strftime("%Y-%m-%d, %H:%M:%S"), temperature, humidity, ))
    sys.stdout.flush()
    measurement = {"humidity": humidity, "temperature": temperature, "measuredAt": str(timestamp)}
    message = TryteString.from_string(json.dumps(measurement))
    tx = ProposedTransaction(address=receiver, value=0, message=message)
    api.send_transfer(depth=1, transfers=[tx])
    print('Sent. Next reading will be taken in {0} seconds.'.format(time_to_sleep))
    time.sleep(time_to_sleep)
