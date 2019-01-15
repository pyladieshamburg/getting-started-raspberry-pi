from iota import Iota

#read the file from the seed file (also change the value of the seed file locally)
in_file = open("tangle/config/seed_tan.conf", "rb") # opening for [r]eading as [b]inary
seed = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

api = Iota('https://durian.iotasalad.org:14265', seed)

# Generate 5 addresses, starting with index 0.
gna_result = api.get_new_addresses(count=5)
addresses = gna_result['addresses']
print(addresses)
