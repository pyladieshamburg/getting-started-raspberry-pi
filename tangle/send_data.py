from datetime import datetime
from iota import Address, Iota, ProposedTransaction, TryteString
import os
with open("tangle/seed.conf") as in_file:
    SEED = in_file.read().rstrip("\n").encode()


with open("tangle/config/address_tan.conf") as in_file:
    ADDRESS = in_file.read().rstrip("\n").encode()

api = Iota("https://durian.iotasalad.org:14265", seed=SEED)

fname = '/Users/stewarta/repos/getting-started-raspberry-pi/pitangle/current_measurements.csv'
f = open(fname)
data = f.read()
f.close()

arr = data.split("\n")
batch_sz = 40
batch = []

for i in len(arr):
    if i%40 == 0:
        # empty list
        batch = []
        # send data
        send_data(str(batch)
    else:
        # append data
        batch.append(arr[i] + "")
        batch.append("\n")


def send_data(data):
    message = TryteString.from_string(data)
    receiver = Address(ADDRESS)
    tx = ProposedTransaction(address=receiver, value=0, message=message)
    api.send_transfer(depth=1, transfers=[tx])
