import os
import requests
import json
from brownie import AdvancedCollectable, network
from metadata import sample_metadata
from scripts.helpful_scripts import get_breed

def main():
    print("Working on " + network.show_active())
    advanced_collectable = AdvancedCollectable[len(AdvancedCollectable) - 1]
    number_of_advanced_collectables = advanced_collectable.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_advanced_collectables)
    )
    write_metadata(number_of_advanced_collectables, advanced_collectable)


def write_metadata(token_ids, nft_contract):
    for token_id in range(token_ids):
        collectable_metadata = sample_metadata.metadata_template
        breed = get_breed(nft_contract.tokenIdToBreed(token_id))
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active())
            + str(token_id)
            + "-"
            + breed
            + ".json"
        )
        if Path(metadata_file_name).exists():
            print(
                "{} already found, delete it to overwrite!".format(
                    metadata_file_name)
            )
        else:
            collectable_metadata["name"] = get_breed(
                nft_contract.tokenIdToBreed(token_id)
            )
            collectable_metadata["description"] = "An adorable {} pup!".format(
                collectable_metadata["name"]
            )
            print(collectable_metadata)
            image_to_upload = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_path = "./img/{}.png".format(breed.lower())
                image_to_upload = upload_to_ipfs(image_path)
                collectable_metadata['image']=image_to_upload
                with open(metadata_file_name, "w") as file:
                json.dump(collectable_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)
            
def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url =("http://localhost:5001")
        response = requests.post(ipfs_url + "/api/v0/add",files={"file": image_binary})
        print(response.json())
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash, filename)
        print(uri)
    return None

