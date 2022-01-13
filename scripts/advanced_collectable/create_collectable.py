from brownie import AdvancedCollectable, accounts, config
from scripts.helpful_scripts import get_breed
import time


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    advanced_collectable = AdvancedCollectable[len(AdvancedCollectable) - 1]
    transaction = advanced_collectable.createCollectable("None", {"from": dev})
    print("Waiting on second transaction...")
    # wait for the 2nd transaction
    transaction.wait(1)
    time.sleep(35)
    requestId = transaction.events["requestedCollectable"]["requestId"]
    token_id = advanced_collectable.requestIdToTokenId(requestId)
    breed = get_breed(advanced_collectable.tokenIdToBreed(token_id))
    print("Dog breed of tokenId {} is {}".format(token_id, breed))