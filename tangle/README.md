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

## And now?

You can find your transaction and message on a tangle explorer, e.g. [https://thetangle.org](https://thetangle.org).

Visit the page and paste in the string you choose for your `Address` to search for all transactions. Then you can click on the individual transaction and display details and the message you attached.
