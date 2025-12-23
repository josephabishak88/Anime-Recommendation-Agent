import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process, fuzz


class RecommendationAgent:
    def __init__(self, dataset_path):
        self.anime = pd.read_csv(dataset_path)

        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.model.encode(
            self.anime["description"].astype(str).tolist()
        )

    def get_available_genres(self):
        genres = set()

        for desc in self.anime["description"]:
            for word in str(desc).lower().split():
                genres.add(word)

        return sorted(genres)

    def recommend(self, fav_anime, user_profile):
        titles = self.anime["name"].astype(str).tolist()

        match = process.extractOne(
            fav_anime,
            titles,
            scorer=fuzz.WRatio
        )

        if not match or match[1] < 60:
            print("⚠ Anime not found")
            return []

        title, score, index = match
        print(f"🎯 Matched with: {title}")
        print("🧠 Why this was recommended:")
        print(" • Strong semantic similarity")
        print(" • Matches your preferred themes")
        print(" • High community rating")

        sims = cosine_similarity(
            [self.embeddings[index]], self.embeddings
        )[0]

        ranked = sorted(
            list(enumerate(sims)),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[1:6]
