from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from embeddings import search_similar_products

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Semantic Product Search Engine Running"}


@app.get("/search")
def search(
    query: str,
    min_price: int = Query(None),
    max_price: int = Query(None),
    sort_by: str = Query("relevance")
):
    results = search_similar_products(
        query_text=query,
        min_price=min_price,
        max_price=max_price,
        sort_by=sort_by
    )

    return {"results": results}