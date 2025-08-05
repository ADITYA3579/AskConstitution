#generate_embeddings

import sys
import os

# Add src/ folder to system path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, 'src')
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

# Import from the newly renamed module
from dataloader_ import load_constitution_data
from embedder import get_model, generate_embeddings, save_embeddings

# Load data and generate embeddings
df = load_constitution_data("data/constitution_of_india.csv")
texts = df['TEXT'].tolist()

model = get_model()
embeddings = generate_embeddings(model, texts)
save_embeddings(embeddings, path="embeddings/constitution_embeddings.pkl")
