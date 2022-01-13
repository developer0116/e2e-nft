from brownie import AdvancedCollectable, accounts, network, config
from scripts.helpful_scripts import get_breed

dict={
        "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=PUG.json",
        "Shiba": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=Shiba.json",
        "Hound": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=Hound.json",
        }


def main():
    print("Working on " + network.show_active())
    advanced_collectable = AdvancedCollectable[len(AdvancedCollectable) - 1]
    number_of_advanced_collectables = advanced_collectable.tokenCounter()
    print("The number of tokens you've deployed is: "+ str(number_of_advanced_collectables))
    for token_id in range(number_of_advanced_collectables):
        breed = get_breed(advanced_collectable.tokenIdToBreed(token_id))
        if not advanced_collectable.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, advanced_collectable,dict[breed])

def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print("Awesome! You can view your NFT")
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')