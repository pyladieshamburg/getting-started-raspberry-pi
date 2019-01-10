#read file and send each line to the tangle

import json


from datetime import datetime
from iota import Address, Iota, ProposedTransaction, TryteString

in_file = open("tangle/address_dump.conf", "rb") # opening for [r]eading as [b]inary
ADDRESS = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

api = Iota("https://durian.iotasalad.org:14265")
receiver = Address(ADDRESS)

with open("pitangle/current_measurements.csv") as f:
    lis=[line.rstrip("\n\r").split(',') for line in f]        # create a list of lists
    for i,x in enumerate(lis):      
        (idx, humidity,ts,temp) = x      #print the list items 
        print(idx)
        measurment = {"humidity":humidity, "temperature":temp,"measuredAt":ts}
        message = TryteString.from_string(json.dumps(measurment))
        tx = ProposedTransaction(address=receiver, value=0, message=message)
        api.send_transfer(depth=1, transfers=[tx])
        



