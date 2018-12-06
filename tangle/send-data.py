from datetime import datetime
from iota import Address, Iota, ProposedTransaction, TryteString

SEED = b"THIS9IS9MY9SEED"

api = Iota("https://durian.iotasalad.org:14265", seed=SEED)

message = TryteString.from_string("Hello PyData Hamburg! It's {}".format(str(datetime.now())))

receiver = Address(b"THEOUTPUTFROMTHEPREVIOUSSTEP")

tx = ProposedTransaction(address=receiver, value=0, message=message)

api.send_transfer(depth=1, transfers=[tx])
