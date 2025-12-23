md
# 🎌 Anime Recommendation AI Agent

## 📌 Project Overview
This project is an AI-powered anime recommendation system built using Natural Language Processing (NLP).  
It suggests anime titles based on semantic similarity, user preferences, and fuzzy text matching.

---

## 🧠 Technologies Used
- Python
- Pandas
- Sentence Transformers (NLP embeddings)
- RapidFuzz (typo-tolerant search)
- Scikit-learn (cosine similarity)

---

## ⚙️ How It Works
1. Anime descriptions are converted into semantic embeddings
2. User input is matched using fuzzy string matching
3. Cosine similarity is used to find related anime
4. Results are ranked and explained to the user

---

## ✨ Features
- Typo-tolerant anime search (e.g., "narut" → Naruto)
- Content-based recommendation system
- Explainable AI outputs
- Programmatically generated dataset
- Scalable and modular design

---

## ▶️ How to Run
```bash
python create_csv.py
python main.py
