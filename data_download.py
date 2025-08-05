# data_download

import requests
import json
import os

# The URL to the JSON dataset
DATASET_URL = "https://storage.googleapis.com/kagglesdsdata/datasets/6580360/10627977/constitution_of_india.json?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20250801%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250801T162607Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=b2401661a07c9a62fe82491c6633100d5a596ab40748e74b4c0a2d961e9268023c0f2410aa65e45a861e547c5e708b46d53480deec9f37f1eea377f452d88ced7812f244b0e8dde0e9248f00fce381fe03085f9d803008f767bce520c8a9a2de6417e20040d8f726760ed624cdb9d4be4b8375c8c03fa45461231cce6d14200fa174b83badf9401f1920360e843bfffdc43850304840d6032671b7a7ff5fdff396bdaac0d7ffe797ab10630d3196317f4ef8dc3f206b0ea7f0ea42d0ca4e30d8c58146459d4d4a007e0282d4dcb9dcb318cf17787609a196342ec9eb25502611e59cdfe59af72ae5fc24e6060fffccf2f754cd3426f54e55334fce2ee8a4cfee"

# The output path where the file will be saved
OUTPUT_PATH = "data/constitution_of_india.json"

def download_json_data(url: str, output_path: str):
    """
    Downloads a JSON file from a URL and saves it to a local file.
    """
    try:
        print(f"Downloading data from {url}...")
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save the JSON content to the file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, indent=4)
        
        print(f"Successfully downloaded and saved data to {output_path}.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    download_json_data(DATASET_URL, OUTPUT_PATH)

