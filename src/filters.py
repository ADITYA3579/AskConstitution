# NER

import spacy
import subprocess
import importlib

try:
    spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
finally:
    nlp = spacy.load("en_core_web_sm")



def keyword_filter(df, keyword):
    """Filter rows where keyword is present in TEXT column."""
    return df[df['TEXT'].str.contains(keyword, case=False, na=False)]

def named_entity_filter(df, entity):
    """Filter rows where the specified named entity appears."""
    filtered_rows = []
    for _, row in df.iterrows():
        doc = nlp(row['TEXT'])
        if any(ent.text.lower() == entity.lower() for ent in doc.ents):
            filtered_rows.append(row)
    return pd.DataFrame(filtered_rows)


