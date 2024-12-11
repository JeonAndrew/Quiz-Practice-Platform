from collections import deque

class User:
    def __init__(self, u_id, email=None):
        self.user_id = u_id
        self.email = email
        self.performance = deque(maxlen=7)  # store last 7 quiz results
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
        if self.recent_quiz is not None and self.recent_quiz.has_submitted():
            self.performance.append(self.recent_quiz.get_result())
            # Could modify streak logic here if desired.

    def get_quiz(self):
        return self.recent_quiz

    def set_quiz(self, quiz):
        self.recent_quiz = quiz

    def get_user_id(self):
        return self.user_id

    def to_dict(self):
        user_data = {
            'user_id': self.user_id,
            'email': self.email,
            'performance': list(self.performance),
            'streak': self.streak,
            # We no longer store recent_quiz details in user doc.
            'recent_quiz': None
        }
        return user_data

    @classmethod
    def from_dict(cls, data):
        user = cls(u_id=data.get('user_id'), email=data.get('email'))
        user.performance = deque(data.get('performance', []), maxlen=7)
        user.streak = data.get('streak', 0)
        # recent_quiz no longer retrieved from Firestore user doc
        return user