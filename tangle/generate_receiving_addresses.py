from iota import Iota

# read the file from the seed file (also change the value of the seed file locally)
with open("tangle/config/seed.conf") as in_file:
    # read as string
    # strip any carriage return characters (Atom, I'm looking at you!)
    # and then encode as bytes()
    seed = in_file.read().rstrip("\n").encode()

api = Iota('https://durian.iotasalad.org:14265', seed)

# Generate 5 addresses, starting with index 0.
gna_result = api.get_new_addresses(count=5)
addresses = gna_result['addresses']
print(addresses)
