# 🛍️ AI Shopping Agent

An AI-powered semantic product search and recommendation system that uses text embeddings and cosine similarity to return meaning-based product results instead of traditional keyword matching.
---
## 📌 Problem Statement

Traditional e-commerce search systems rely on keyword matching.
If users search using different words (e.g., "gym footwear" instead of "running shoes"), relevant results may not appear.

This project solves that by implementing semantic search using vector embeddings and similarity scoring.
---
## 🛠 Tech Stack
Frontend
-React.js
-Axios
-CSS
Backend
-FastAPI
-Python
-NumPy
-Pickle (for storing embeddings)
---
## 🚀 Features
- 🔍 Semantic product search using transformer embeddings
- Cosine similarity ranking
- Price-based sorting (Low → High, High → Low)
- REST API architecture
- Interactive frontend UI
- Dark mode toggle
- 🧠 AI-based product recommendations  
- 📊 User interaction logging  
- ⚡ FastAPI backend  
- 💻 React frontend  
---
## 🧠 How It Works

1.User enters a search query.
2.Backend converts the query into an embedding vector.
3.Stored product embeddings are compared using cosine similarity.
4.Products are ranked by similarity score.
5.Results are optionally sorted by price.
6.JSON response is sent back to frontend.
7.React displays results dynamically.
---
## 🏗 Architecture

Frontend (React)
⬇ HTTP Request
Backend (FastAPI)
⬇
Embedding Generator
⬇
Cosine Similarity Engine
⬇
Sorted Results
⬇
JSON Response
⬇
Frontend Rendering
---

## 🏗️ Project Structure

AI-Shopping-Agent/
│
├── backend/
│   ├── app.py
│   ├── recommender.py
│   ├── embeddings.py
│   ├── models.py
│   ├── database.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── components/
│
└── README.md
---
## ▶️ How to Run Locally
Backend
-cd backend
-pip install -r requirements.txt
-uvicorn app:app --reload
Frontend
-cd frontend
-npm install
-npm start
---
## 📈 Future Improvements

Replace local embeddings with OpenAI embeddings
Use vector database (FAISS / Pinecone)
Add authentication
Add pagination
Dockerize application
Deploy to cloud (Render + Vercel)
---

## ⚙️ Setup Instructions

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload



