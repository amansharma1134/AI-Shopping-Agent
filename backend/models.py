import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def train_recommender():
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.abspath(
    os.path.join(BASE_DIR, ".." , "data" , "products.csv")
    )

    products = pd.read_csv(file_path)

    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(products["description"])

    return tfidf, tfidf_matrix, products