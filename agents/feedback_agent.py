class FeedbackAgent:
    def get_feedback(self):
        response = input(
            "Did you like these recommendations? (yes/no): "
        )
        return response.lower() == "yes"
