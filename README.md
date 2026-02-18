# 🛍️ AI Shopping Agent

An AI-powered semantic product search and recommendation system that uses text embeddings and cosine similarity to return meaning-based product results instead of traditional keyword matching.
---

## 🚀 Features

- 🔍 Semantic product search using transformer embeddings  
- 🧠 AI-based product recommendations  
- 📊 User interaction logging  
- ⚡ FastAPI backend  
- 💻 React frontend  

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

## 🧠 Tech Stack

- Python
- FastAPI
- Sentence Transformers
- SQLite
- React
- Git & GitHub

---

## ⚙️ Setup Instructions

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload

