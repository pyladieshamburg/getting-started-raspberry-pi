from datetime import datetime
from iota import Address, Iota, ProposedTransaction, TryteString

in_file = open("tangle/config/seed.conf", "rb") # opening for [r]eading as [b]inary
SEED = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

in_file = open("tangle/config/address.conf", "rb") # opening for [r]eading as [b]inary
ADDRESS = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

api = Iota("https://durian.iotasalad.org:14265", seed=SEED)

message = TryteString.from_string("Hello PyLadies Hamburg! It's {}".format(str(datetime.now())))

receiver = Address(ADDRESS)

tx = ProposedTransaction(address=receiver, value=0, message=message)

api.send_transfer(depth=1, transfers=[tx])
