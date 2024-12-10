from collections import deque

class User:
    def __init__(self, uid):
        self.user_id = uid
        self.performance = deque(maxlen = 7)  # To store the last 7 quiz results
        self.streak = 0
        self.recent_quiz = None

    def reset_streak(self):
        self.streak = 0

    def get_streak(self):
        return self.streak

    def add_to_streak(self):
        self.streak += 1

    def get_performance(self):
        return list(self.performance) 

    def set_latest_performance(self):
        if len(self.performance) >= 7:
            self.performance.popleft() 
        if self.recent_quiz:
            self.performance.append(self.recent_quiz.get_result()) 

    def get_quiz(self):
        return self.recent_quiz

    def set_quiz(self, quiz):
        self.recent_quiz = quiz
        self.set_latest_performance()

    def get_user_id(self):
        return self.user_id
