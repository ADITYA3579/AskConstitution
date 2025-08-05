# app

import streamlit as st
from src.dataloader_ import load_constitution_data
from src.embedder import get_model, load_embeddings
from src.retriever import semantic_search
from src.qna_generator import load_qa_model, answer_query
from src.utils import format_result
from src.filters import keyword_filter, named_entity_filter

# Title
st.title("AskConstitution: Indian Constitution Assistant")

# Load everything
df = load_constitution_data("data/constitution_of_india.csv")
model = get_model()
embeddings = load_embeddings("embeddings/constitution_embeddings.pkl")
qa_model = load_qa_model()

# Sidebar Filters
st.sidebar.header("Filters")
keyword = st.sidebar.text_input("Filter by keyword (e.g. education, amendment):")
named_entity = st.sidebar.text_input("Filter by named entity (e.g. Parliament, President):")

# Main Input
query = st.text_input("Enter your legal/constitutional question")

# Handle Filters First
if keyword:
    st.subheader("Filtered by Keyword")
    filtered_df = keyword_filter(df, keyword)
    if filtered_df.empty:
        st.warning("No articles found with that keyword.")
    else:
        for _, row in filtered_df.iterrows():
            st.markdown(format_result(row['article'], row['title'], row['description']))

elif named_entity:
    st.subheader("Filtered by Named Entity")
    filtered_df = named_entity_filter(df, named_entity)
    if filtered_df.empty:
        st.warning("No articles found with that named entity.")
    else:
        for _, row in filtered_df.iterrows():
            st.markdown(format_result(row['article'], row['title'], row['description']))

# Then handle Q&A
elif query:
    results, _ = semantic_search(query, model, embeddings, df, top_k=3)
    st.subheader("Top Relevant Articles")
    for _, row in results.iterrows():
        st.markdown(format_result(row['article'], row['title'], row['description']))

    st.subheader("Answer")
    answer = answer_query(qa_model, query, results.iloc[0]['TEXT'])
    st.success(answer)
