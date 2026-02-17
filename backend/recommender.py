import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("products.csv")

# Combine title + description
df["text"] = df["title"] + " " + df["description"]

# Create TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["text"])


def recommend_products(user_query, user_id="guest", top_k=5, sort_by="similarity"):
    query_vec = vectorizer.transform([user_query])
    similarity = cosine_similarity(query_vec, tfidf_matrix)

    df["similarity"] = similarity[0]

    if sort_by == "price_low":
        df_sorted = df.sort_values(by="price", ascending=True)
    elif sort_by == "price_high":
        df_sorted = df.sort_values(by="price", ascending=False)
    else:
        df_sorted = df.sort_values(by="similarity", ascending=False)

    top_results = df_sorted.head(top_k)

    results = []
    for _, row in top_results.iterrows():
        results.append({
            "product_name": row["title"],
            "description": row["description"],
            "price": float(row["price"]),
            "score": float(row["similarity"])
        })

    return results