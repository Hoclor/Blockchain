import hashlib
import ecdsa
import binascii
import math

# An the previous block header - do not change any fields
previous_block_header = {
  "previousBlockHash": "651c16a0226d2ddd961c9391dc11f703c5972f05805c4fb45ab1469dda1d4b98",
  "payloadLength": 209,
  "totalAmountNQT": "383113873926",
  "generationSignature": "9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1",
  "generator": "11551286933940986965",
  "generatorPublicKey": "feb823bac150e799fbfc124564d4c1a72b920ec26ce11a07e3efda51ca9a425f",
  "baseTarget": 1229782938247303,
  "payloadHash": "06888a0c41b43ad79c4e4991e69372ad4ee34da10d6d26f30bc93ebdf7be5be0",
  "generatorRS": "NXT-MT4P-AHG4-A4NA-CCMM2",
  "nextBlock": "6910370859487179428",
  "requestProcessingTime": 0,
  "numberOfTransactions": 1,
  "blockSignature": "0d237dadff3024928ea4e5e33613413f73191f04b25bad6b028edb97711cbd08c525c374c3e2684ce149a9abb186b784437d01e2ad13046593e0e840fd184a60",
  "transactions": ["14074549945874501524"],
  "version": 3,
  "totalFeeNQT": "200000000",
  "previousBlock": "15937514651816172645",
  "cumulativeDifficulty": "52911101533010235",
  "block": "662053617327350744",
  "height": 2254868,
  "timestamp": 165541326
}

# you should edit the effective balance to be the last two digits from your user id
effective_balance = 24 # My user ID is pbqk24

# Generate an ECDSA key pair (use the same private/public key pair)
signing_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
verifying_key = signing_key.get_verifying_key()

print("Private key: {}".format(binascii.hexlify(signing_key.to_string())))
print("Public key: {}".format(binascii.hexlify(verifying_key.to_string())))

# Sign the message "Hello world"
signature = signing_key.sign(b"Hello world")
print("Signature of 'Hello world': {}".format(binascii.hexlify(signature)))

# Verify the above signature
verified = verifying_key.verify(signature, b"Hello world")
if verified:
  print("Signature successfully verified")
else:
  print("Signature not verified")

# Compute the hit value
# Sign the previous block generation signature
block_sig = signing_key.sign(previous_block_header['generationSignature'].encode())
print("Signature used for calculating the hit value: {}".format(binascii.hexlify(block_sig)))
# Hash the signature
block_sig_hash = hashlib.sha256(block_sig).hexdigest()
# Take the first 8 bytes of the hash as the hit value (i.e. first 16 hex digits)
hit_value = block_sig_hash[:16]

print("Hit value: {}".format(hit_value))

# Determine how long (in seconds) after the publication of the previous block you would be able to forge a new block

# Compute the target value
target = previous_block_header['baseTarget'] * effective_balance
# real target is target * time in seconds
# Thus, time when I can forge a new block = hit_value / target
seconds = int(hit_value, base=16)/target
print("Seconds to forge new block: {}".format(math.ceil(seconds)))

# Report values
# ECDSA public key (in hex): 4f045a6cfacb3e67e7c5d4ddfb9f1acfe7d6dddac29869734cce5218cdab24e2d2cc72601138d6f324464df7691f819cd14e8b3752d9c463e5162aad37393ca0
# The signature of "Hello world" (in hex): eae12ab8fdbeb5635ac45edbfceb999907a5b09042eeddbd9a07a744f656b3ac7e00124086256e5caf86539e68186742d593e5e8b537b9f6d7ee05557c2ef68a
# The signature used in calculating the hit value (in hex): 
# My hit value (in hex): 
# The time in seconds when you would be able to forge a new block: 