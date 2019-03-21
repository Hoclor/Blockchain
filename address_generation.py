import blockcypher

address = blockcypher.generate_new_address(coin_symbol='btc-testnet', api_key='api_key')

print(address)
# address: mvcM9NV5hesnSUNpZGZ9Pyt3PK8xDFmCTp
# private: a62563d8a5a01a725c511ea1c7d3b6b03e4469c004228baef97bccc226c47cde
# public:  0388b0bbbfd432f0a2b752952cbef2c83a3efd48cf6d1f99a73d789f55a65a236f
# wif:     cT9fgw8se64uUTvv6KcqdtcTczQKLdRBfnJKjtQTypGXYCqQduhV