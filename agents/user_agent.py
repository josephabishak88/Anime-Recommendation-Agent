class UserAgent:
    def get_preferences(self):
        print("\nPlease enter your preferences")

        genres = input(
            "Enter preferred genres (comma separated): "
        ).split(",")

        min_rating = float(
            input("Enter minimum rating (e.g. 7.5): ")
        )

        return {
            "genres": [g.strip().lower() for g in genres],
            "min_rating": min_rating
        }
