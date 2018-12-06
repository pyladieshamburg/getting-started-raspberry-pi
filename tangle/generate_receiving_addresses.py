from iota import Iota

api = Iota('https://durian.iotasalad.org:14265', b'THIS9IS9MY9SEED')

# Generate 5 addresses, starting with index 0.
gna_result = api.get_new_addresses(count=5)
addresses = gna_result['addresses']
print(addresses)
