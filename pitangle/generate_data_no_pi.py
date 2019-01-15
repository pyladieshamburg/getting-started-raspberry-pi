# read file and send each line to the tangle
import json

from iota import Address, Iota, ProposedTransaction, TryteString

with open("tangle/address_dump.conf") as in_file:
    ADDRESS = in_file.read().rstrip("\n").encode()

api = Iota("https://durian.iotasalad.org:14265")
receiver = Address(ADDRESS)

with open("pitangle/current_measurements.csv") as f:
    lis = [line.rstrip("\n\r").split(",") for line in f]        # create a list of lists
    for i, x in enumerate(lis):
        (idx, humidity, ts, temp) = x      # print the list items
        print(idx)
        measurment = {"humidity": humidity, "temperature": temp, "measuredAt": ts}
        message = TryteString.from_string(json.dumps(measurment))
        tx = ProposedTransaction(address=receiver, value=0, message=message)
        api.send_transfer(depth=1, transfers=[tx])
