#retriever

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def semantic_search(query, model, corpus_embeddings, df, top_k=5):
    query_emb = model.encode([query])
    scores = cosine_similarity(query_emb, corpus_embeddings)[0]
    top_k_idx = np.argsort(scores)[::-1][:top_k]
    return df.iloc[top_k_idx], scores[top_k_idx]

