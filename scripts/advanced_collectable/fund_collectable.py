from brownie import AdvancedCollectable

from scripts.helpful_scripts import fund_advanced_collectable

def main():
    advanced_collectable=AdvancedCollectabe[len(AdvancedCollectable)-1]
    fund_advanced_collectable(advanced_collectable)