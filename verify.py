import ecdsa

# put the hex of your public key in the line below
vk_string="1df3790aa29735e11912270b150f8c3e86e5421e68b52a0a43f69fd020d3482a37e48d87ee4bef20763002dfc7dbaa160e9a154dd4d6967b573f16f66b546037"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string),ecdsa.SECP256k1)

message = b'Hello world'

# put your signature for Hello world in the line below
sig_hex = "87e91f8a3a25149e2c6f172bbfcedde78d29d0c3a7cfbf535d39d71d5b08cf9974ae48d2bc9546444240a3c3087dcf58c974ded04d1a3255b54e0dde6af075eb"
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