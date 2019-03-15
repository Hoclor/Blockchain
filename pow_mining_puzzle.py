import hashlib
import json
import time

# An example block header - do not change any fields except nonce and coinbase_addr
example_block_header = {'height': 1478503,
                        'prev_block': '0000000000000da6cff8a34298ddb42e80204669367b781c87c88cf00787fcf6',
                        'total': 38982714093,
                        'fees': 36351,
                        'size': 484,
                        'ver': 536870912,
                        'time': 1550603039.882228,
                        'bits': 437239872,
                        'nonce': 0,                     #You may change this field of the block
                        'coinbase_addr': 'pbqk24',     #You should change this field of the block to your studentID
                        'n_tx': 2,
                        'mrkl_root': '69224771b7a2ed554b28857ed85a94b088dc3d89b53c2127bfc5c16ff49da229',
                        'txids': ['3f9dfc50198cf9c2b0328cd1452513e3953693708417440cd921ae18616f0bfc', '3352ead356030b335af000ed4e9030d487bf943089fc0912635f2bb020261e7f'],
                        'depth': 0}

# Simplified conversion of block header into bytes:
block_serialised = json.dumps(example_block_header, sort_keys=True).encode()

# Double SHA256 hashing of the serialised block
block_hash=hashlib.sha256(hashlib.sha256(block_serialised).digest()).hexdigest()
print('Hash with nonce ' + str(example_block_header['nonce'])+': '+block_hash)

# Calculate the target value with a difficulty of 0.001
initial_target = 0x00000000FFFF0000000000000000000000000000000000000000000000000000
current_target = initial_target * 1000 # same as / 0.001

print("Target value:    0x00000{}".format(hex(current_target)[2:]))

time.sleep(3) # Wait 3 seconds before beginning block mining

# Time the mining
start = time.time()
# Find a nonce that makes the block valid
while(int(block_hash, base=16) > current_target):
    # Print progress report every 100000 nonces
    if example_block_header['nonce'] % 100000 == 0:
        print("Current nonce: {}".format(example_block_header['nonce']))
    
    # Increment the nonce
    example_block_header['nonce'] += 1

    # Recalculate the hash of the block

    # Simplified conversion of block header into bytes:
    block_serialised = json.dumps(example_block_header, sort_keys=True).encode()

    # Double SHA256 hashing of the serialised block
    block_hash=hashlib.sha256(hashlib.sha256(block_serialised).digest()).hexdigest()
time_taken = time.time() - start

# Estimate time required if difficulty = 1 (initial bitcoin difficulty)

# Estimate time required if difficulty = 7454968648263

# Calculation: hash_space_size = 2^256, hashes required to find a valid target = hash_space_size/target
# Time required to find such a hash = time_per_hash*hashes_required
# where time_per_hash = time_taken/hashes_performed

print("Final nonce: {}".format(example_block_header['nonce']))
print("Hash with this nonce: {}".format(block_hash))
print("Found in {} seconds".format(time_taken))

time_per_hash = time_taken/example_block_header['nonce']
print("Time per hash: {}".format(time_per_hash))

diff_1_target = initial_target
diff_1_hashes = 2**256//diff_1_target
diff_1_time = time_per_hash*diff_1_hashes

diff_high_target = initial_target / 7454968648263
diff_high_hashes = 2**256//diff_high_target
diff_high_time = time_per_hash*diff_high_hashes
print()
print("Time if difficulty = 1:")
print("Target = {}".format(diff_1_target))
print("Hashes required = {}".format(diff_1_hashes))
print("Time required: {}".format(diff_1_time))
print()
print("Time if difficulty = 7454968648263:")
print("Target = {}".format(diff_high_target))
print("Hashes required = {}".format(diff_high_hashes))
print("Time required: {}".format(diff_high_time))

#TEMP - values for the report
# Block hash target: 0x000003e7fc180000000000000000000000000000000000000000000000000000
# Nonce (int): 2171906
# Double hashes performed to find this nonce value: 2171907
# Time taken for diff 1: 3070496729011 seconds
# Time taken for diff 7454968648263: 2.289 * 10^25 seconds
# Block hash:        0x0000007c39960407fb9c5f22fa73359e92d8f58e16e7a47e227743798b2f80b8