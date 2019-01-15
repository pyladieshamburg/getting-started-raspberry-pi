from datetime import datetime
from iota import Address, Iota, ProposedTransaction, TryteString

with open("tangle/config/seed_tan.conf") as in_file:
    SEED = in_file.read().rstrip("\n").encode()


with open("tangle/config/address_tan.conf") as in_file:
    ADDRESS = in_file.read().rstrip("\n").encode()

api = Iota("https://durian.iotasalad.org:14265", seed=SEED)

message = TryteString.from_string("Hello PyLadies Hamburg! It's {}".format(str(datetime.now())))

receiver = Address(ADDRESS)

tx = ProposedTransaction(address=receiver, value=0, message=message)

api.send_transfer(depth=1, transfers=[tx])
