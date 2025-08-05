#embedder

from sentence_transformers import SentenceTransformer
import joblib

def get_model(model_name="all-MiniLM-L6-v2"):
    return SentenceTransformer(model_name)

def generate_embeddings(model, texts):
    return model.encode(texts, show_progress_bar=True)

def save_embeddings(embeddings, path="embeddings_constitution.pkl"):
    joblib.dump(embeddings, path)

def load_embeddings(path="embeddings_constitution.pkl"):
    return joblib.load(path)