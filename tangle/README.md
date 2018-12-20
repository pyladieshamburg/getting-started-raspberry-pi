# PyOTA

## Install

Install pyota lib with:

```
pip3 install pyota
```

## Configuration

Create a new file `generate_receiving_addresses.py` with the following content. Remember to replace the seed (the part that reads `b'THIS9IS9MY9SEED'`) with a seed of your choosing. Allowed characters are A-Z and 9.

```python

from iota import Iota

api = Iota('https://durian.iotasalad.org:14265', b'THIS9IS9MY9SEED')

# Generate 5 addresses, starting with index 0.
gna_result = api.get_new_addresses(count=5)
addresses = gna_result['addresses']
print(addresses)
```

Save the file and run it. It will display an address that you can use as receiver for your data in the next file, e.g.:

```bash
 $ python3 generate_receiving_addresses.py
[Address(b'YMPXYZUKTLAOUR9AJVMHCI9RCZERCIREXXXD9QOUOUKIKQHWFCWRFZYYVPMPHFJA9GSQVFUVQ9HGRZYPW')]
```

## Send data to the Tangle

Create another file `send_data.py`. Replace the `SEED` with the same seed you chose for the previous file and the address as well.

```python
from datetime import datetime
from iota import Address, Iota, ProposedTransaction, TryteString

SEED = b"THIS9IS9MY9SEED"

api = Iota("https://durian.iotasalad.org:14265", seed=SEED)

message = TryteString.from_string("Hello PyData Hamburg! It's {}".format(str(datetime.now())))

receiver = Address(b"YMPXYZUKTLAOUR9AJVMHCI9RCZERCIREXXXD9QOUOUKIKQHWFCWRFZYYVPMPHFJA9GSQVFUVQ9HGRZYPW")

tx = ProposedTransaction(address=receiver, value=0, message=message)

api.send_transfer(depth=1, transfers=[tx])
```

Save the file and execute it to send a message to the tangle.

## Read data from the Tangle

Create yet another file `read_data.py`. Again, replace the `Address` with the address you generated for yourself in the **Configuration** step.

```python
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
```

Save the file and execute it to print all messages stored on your `Address`.

## And now?

You can find your transaction and message on a tangle explorer, e.g. [https://thetangle.org](https://thetangle.org).

Visit the page and paste in the string you chose for your `Address` to search for all transactions. Then you can click on the individual transaction and display details and the message you attached.
