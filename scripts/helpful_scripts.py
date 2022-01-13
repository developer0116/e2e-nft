from brownie import AdvancedCollectable,accounts,network,config,interface

def fund_advanced_collectable(nft_contract):
    dev =accounts.add(config['wallets']['from_key'])
    link_token = interface.LinkTokenInterface(config['networks'][network.show_active()]['link_token'])
    link_token.transfer(nft_contract,10000000000000000,{'from':dev})

def get_breed(breed_number):
    switch = {0: "PUG", 1: "Shiba", 2: "Hound"}
    return switch[breed_number]