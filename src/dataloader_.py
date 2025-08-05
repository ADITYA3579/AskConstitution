#data_loader

import pandas as pd

def load_constitution_data(path="data/constitution_of_india.csv"):
    df = pd.read_csv(path)
    df.dropna(subset=['title', 'description'], inplace=True)
    df['TEXT'] = df['title'].str.strip() + ". " + df['description'].str.strip()
    return df




