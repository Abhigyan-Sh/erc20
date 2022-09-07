from brownie import accounts, network, config

LOCAL_DEVELOPMENT_NETWORK= ['development', 'ganache-cli']

def get_account(id= None, index= None): # using python default arguments..
    if id:
        return accounts.load(id)
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_DEVELOPMENT_NETWORK:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
