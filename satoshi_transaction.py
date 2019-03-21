import blockcypher

#Specify the inputs and outputs below
#For convenince you can specify an address, and the backend will work out what transaction output that address has available to spend
#You do not need to list a change address, by default the transaction will be created with all change (minus the fees) going to the first input address
inputs = [{'address': 'mvcM9NV5hesnSUNpZGZ9Pyt3PK8xDFmCTp'}]
outputs = [{'address': 'mpamtqLA66JFVSQNDaPHZ5xMiCz6T2MeNn', 'value': 100}]
#The next line creates the transaction shell, which is as yet unsigned
unsigned_tx = blockcypher.create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='btc-testnet', api_key='api_key')
#You can edit the transaction fields at this stage, before signing it.


#Now list the private and public keys corresponding to the inputs
private_keys=['a62563d8a5a01a725c511ea1c7d3b6b03e4469c004228baef97bccc226c47cde']
public_keys=['0388b0bbbfd432f0a2b752952cbef2c83a3efd48cf6d1f99a73d789f55a65a236f']
#Next create the signatures
tx_signatures = blockcypher.make_tx_signatures(txs_to_sign=unsigned_tx['tosign'], privkey_list=private_keys, pubkey_list=public_keys)
#Finally push the transaction and signatures onto the network
blockcypher.broadcast_signed_transaction(unsigned_tx=unsigned_tx, signatures=tx_signatures, pubkeys=public_keys, coin_symbol='btc-testnet', api_key='api_key')

print(unsigned_tx)
