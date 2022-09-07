from scripts.helpful_scripts import get_account
from brownie import MyToken, network, config
from web3 import Web3

def deployer():
    account= get_account()
    supplyOf= 99*10**20
    erc20= MyToken.deploy(supplyOf,{"from":account},
    publish_source= config["networks"][network.show_active()].get("verify", False))
    # @dev::: erc20= MyToken.deploy(supplyOf,'simpToken','smpT',{"from":account})
    print(f'created a supply of {supplyOf} simpTokens')
# @dev::: deployed to: 0xb89a23e71c0f72a900AF0407Cf17f4612e72D426

def getname_n_symbol():
    erc20= MyToken[-1]
    print(f"Name: {erc20.name()}, Symbol: {erc20.symbol()}") # since not a transaction
# @dev::: and to run this method the way intended we will run it by specifying the same network

def get_totalSupply():
    erc20= MyToken[-1]
    supply= erc20.totalSupply()
    print(f'Total number of tokens are {Web3.fromWei(supply,"ether")} simpToken')

def balanceOfAccount(acnt):
    erc20= MyToken[-1]
    balanceOf= erc20.balanceOf(acnt)
    print(f'balance of account is {Web3.fromWei(balanceOf,"ether")} simpTokens')

def transferTo():
    # toAddress= '0xF3a3bAeaC912841D7DE6afED3292855C20dcab25' # from metamask wallet
    toAddress= config['networks'][network.show_active()]["account2"]
    erc20= MyToken[-1]
    txn1= erc20.transfer(toAddress, Web3.toWei(4500, "ether"), {"from":get_account()})
    txn1.wait(1)
    balanceOfAccount(toAddress)

def transfer_fromTo(): # didn't worked
    erc20= MyToken[-1]
    toAddress= config['networks'][network.show_active()]["account2"]
    # didn't worked ???
    txn2= erc20.allowance(get_account(), toAddress)
    # txn2.wait(1)
    # 
    txn1= erc20.transferFrom(toAddress, get_account(), Web3.toWei(1000, "ether"), 
    {"from":get_account(), "gas_limit": 10000000000000000, "allow_revert": True}).estimateGas(get_account())
    txn1.wait(1)

# @dev::: The following setting in brownie-config.yaml worked for me:
# @dev::: settings:
# @dev:::    gas_limit: "100000000000"

# @dev::: ValueError: Execution reverted during call: 'execution reverted: ERC20: transfer amount exceeds allowance'. This transaction will likely revert. If you wish to broadcast, include `allow_revert:True` as a transaction parameter.
    balanceOfAccount(toAddress)
    # initially: (metamask accounts)
       # account1: 5400 = get_account()
       # account2: 4500
    # later:
       # account1: 6400
       # account2: 3500

def incrementToken():
    erc20= MyToken[-1]
    account= get_account()
    txn1= erc20._mint(account, Web3.toWei(1000, "ether"))
    txn1.wait(1)
    balanceOfAccount(account)
# @dev::: similarly _burn reduces total supply (not working)

def main():
    # deployer()
    # getname_n_symbol
    # get_totalSupply()
    # balanceOfAccount(get_account())
    # transferTo()
    # transfer_fromTo()
    # incrementToken()

    # print(Web3.toWei(.5, "finney"))

    # txn= MyToken[-1].sendo({"from": get_account()})
    # txn.wait(1)
    pass
