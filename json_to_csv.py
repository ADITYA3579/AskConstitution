# convert_json_to_csv

import pandas as pd
import json
import os

# Define the paths for your input JSON and output CSV files
INPUT_JSON_PATH = "../data/constitution_of_india.json"
OUTPUT_CSV_PATH = "../data/constitution_of_india.csv"


def convert_json_to_csv(json_path: str, csv_path: str):
    """
    Converts a JSON file to a CSV file.
    """
    try:
        if not os.path.exists(json_path):
            print(f"Error: The JSON file at '{json_path}' was not found.")
            return False

        # Load the JSON data
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert the list of dictionaries to a pandas DataFrame
        df = pd.DataFrame(data)

        # Save the DataFrame to a CSV file
        df.to_csv(csv_path, index=False)
        
        print(f"Successfully converted '{json_path}' to '{csv_path}'.")
        return True
    
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return False

if __name__ == "__main__":
    convert_json_to_csv(INPUT_JSON_PATH, OUTPUT_CSV_PATH)

