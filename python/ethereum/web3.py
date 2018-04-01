#python
#ethereum
#web3.py

# connection to Blockchain
from web3 import Web3, HTTPProvider, IPCProvider
web3 = Web3(HTTPProvider('http://localhost:8545'))

#accounts
accs = web3.eth.accounts
-->['0x627306090abaB3A6e1400e9345bC60c78a8BEf57', ...]
public keys

#sendTransaction
web3.eth.sendTransaction({'to': accs[1], 'from': accs[0], 'data': "ExampleData", 'value':123})
-->0xef046782fcd2fa72c0080b713c6534937a9e043e2cd56065bcca19051dc6e3b0

#contract
from web3.contract import ConciseContract
#read json
import json
with open('abi.json', 'r') as abi_definition:
    abi = json.load(abi_definition)

myContract = web3.eth.contract(
  contractAddress,
  abi=abi,
  ContractFactoryClass=ConciseContract
)
#send Data to Contract
myContract.methodeName(para1, para2, transact={'from': accs[1]})
-->0x597ac2702242ec53df55a8d45be675c4466f8f5e6965e75551a2b0319f0b2380'
