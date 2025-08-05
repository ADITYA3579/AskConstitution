# AskConstitution 

A modular, interactive **Q&A and semantic search app** built using the **Indian Constitution** dataset. This project uses **sentence-transformer embeddings**, **transformers for Q&A**, **keyword and named entity filters**, and a **Streamlit UI** to allow users to query Indian constitutional content in natural language.

---

##  Features

- **Semantic Search**: Retrieve the most relevant articles from the Indian Constitution.
- **Q&A Model**: Ask natural language questions and receive answers from the content.
- **Keyword & Entity Filters**: Filter content by keywords or named entities like "President", "Parliament", etc.
- **Modular Code**: Each module is separated for clean, maintainable design (`dataloader`, `embedder`, `retriever`, `filters`, etc.)
- **Streamlit UI**: Simple and intuitive interface.

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ADITYA3579/AskConstitution.git
cd AskConstitution
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Prepare the Data

If starting from JSON:

```bash
python src/json_to_csv.py
```

Then, generate embeddings:

```bash
python generate_embeddings.py
```

### 4. Run the App

```bash
streamlit run app.py
```

---

##  Example Queries

- What are the powers of the President?
- Duties of the Prime Minister?
- What is Article 370?
- What does the Constitution say about Emergency?

---

##  Credits

- Built using [HuggingFace Transformers](https://huggingface.co/), [SentenceTransformers](https://www.sbert.net/), [SpaCy](https://spacy.io/), and [Streamlit](https://streamlit.io/)

---

##  Future Plans

- Add **RAG-style** answer generation
- Integrate **LangChain** for agent-style pipelines
- Visualize structure via **timeline** or **article graph**

---

##

