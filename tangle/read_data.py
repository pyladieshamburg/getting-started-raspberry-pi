from datetime import datetime
from iota import Address, Iota, Transaction, TryteString

# 0. Where is data stored?
receiver = Address(
    b"YMPXYZUKTLAOUR9AJVMHCI9RCZERCIREXXXD9QOUOUKIKQHWFCWRFZYYVPMPHFJA9GSQVFUVQ9HGRZYPW"
)

# 1. Connect to public node
api = Iota("https://durian.iotasalad.org:14265")

# 2. Retrieve all transactions
txs = api.find_transactions(addresses=[receiver])

# 3. Iterate over transactions, decode and print
for tx_hash in txs["hashes"]:
    tx_hash_b = bytes(tx_hash)
    tx_data_trytes = api.get_trytes([tx_hash_b])
    tryte_str = str(tx_data_trytes["trytes"][0])

    tx = Transaction.from_tryte_string(tryte_str)

    timestamp = datetime.fromtimestamp(tx.timestamp)
    tx_data = str(tx.signature_message_fragment.decode())
    print("{ts}: {tx}".format(ts=timestamp, tx=tx_data))
