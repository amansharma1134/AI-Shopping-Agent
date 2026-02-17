import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load local transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------------
# CREATE REAL EMBEDDINGS
# -----------------------------
def create_embeddings():
    df = pd.read_csv("products.csv")

    texts = df["description"].tolist()
    embeddings = model.encode(texts)

    df["embedding"] = embeddings.tolist()

    with open("products_with_embeddings.pkl", "wb") as f:
        pickle.dump(df, f)

    print("Real local embeddings created and saved.")


# -----------------------------
# SEARCH SIMILAR PRODUCTS
# -----------------------------
def search_similar_products(
    query_text,
    top_k=5,
    min_price=None,
    max_price=None,
    sort_by="relevance"
):
    with open("products_with_embeddings.pkl", "rb") as f:
        df = pickle.load(f)

    # Generate query embedding
    query_embedding = model.encode([query_text])

    product_embeddings = np.array(df["embedding"].tolist())

    similarities = cosine_similarity(query_embedding, product_embeddings)[0]

    df["score"] = similarities

    # Apply price filters
    if min_price is not None:
        df = df[df["price"] >= min_price]

    if max_price is not None:
        df = df[df["price"] <= max_price]

    # Sorting
    if sort_by == "price":
        df = df.sort_values(by="price", ascending=True)
    else:
        df = df.sort_values(by="score", ascending=False)

    return df.head(top_k).to_dict(orient="records")