from agents.user_agent import UserAgent
from agents.recommendation_agent import RecommendationAgent
from agents.feedback_agent import FeedbackAgent


def main():
    print("🎌 Anime Recommendation AI Agent Started")

    user_agent = UserAgent()
    rec_agent = RecommendationAgent("data/anime.csv")
    available_genres = rec_agent.get_available_genres()

    print("\n📚 Available genre keywords:")
    print(", ".join(available_genres[:20]), "...")

    feedback_agent = FeedbackAgent()

    profile = user_agent.get_preferences()
    fav_anime = input("Enter your favorite anime: ")

    recommendations = rec_agent.recommend(fav_anime, profile)

    if not recommendations:
        print("❌ No recommendations available. Try another anime.")
        return

    print("\n🌟 Recommended Anime:\n")

    for i, (idx, score) in enumerate(recommendations, 1):
        anime_name = rec_agent.anime.iloc[idx]["name"]
        print(f"{i}. {anime_name}")

    feedback = feedback_agent.get_feedback()

    if feedback:
        print("👍 Thanks for your feedback!")
    else:
        print("👌 Feedback noted.")


if __name__ == "__main__":
    main()
