import ecdsa

# put the hex of your public key in the line below
vk_string="4f045a6cfacb3e67e7c5d4ddfb9f1acfe7d6dddac29869734cce5218cdab24e2d2cc72601138d6f324464df7691f819cd14e8b3752d9c463e5162aad37393ca0"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string),ecdsa.SECP256k1)

message = b'Hello world'

# put your signature for Hello world in the line below
sig_hex = "c2761ab46b3849ca44fa3b27512a7ed953a09b5bd8f6c46e30b2e4519dc74b8a1ffa1efb903f10d1874b6f654169f1594c5284ad6e58e98454af11831ebc798e"
sig = bytes.fromhex(sig_hex)

print("Checking signature")
print("Message: "+str(message))

print("Signature: "+sig_hex)
print("Public key: "+vk_string)
try:
    vk.verify(sig, message)# True
    print('Verification passed')
except ecdsa.keys.BadSignatureError:
    print('Verification failed')