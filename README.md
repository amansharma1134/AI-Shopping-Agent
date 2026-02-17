# 🛍️ AI Shopping Agent

An AI-powered shopping assistant that enables semantic product search and personalized recommendations using NLP and FastAPI.

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
├── backend/        # API & AI logic
├── frontend/       # User interface
├── data/           # Dataset files
├── notebooks/      # Experiments
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
