import random
from models.Question import Question

class Topic:
    kMaxProficiency = 20

    def __init__(self, name, t_id, proficiency, active=True):
        self.topic_name = name
        self.topic_id = t_id
        self.proficiency = proficiency
        self.active = active
        self.questions = []

    def get_name(self):
        return self.topic_name

    def increment(self):
        if self.proficiency < self.kMaxProficiency:
            self.proficiency += 1

    def decrement(self):
        if self.proficiency > 0:
            self.proficiency -= 1

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def add_question(self, question):
        self.questions.append(question)

    def get_proficiency(self):
        return self.proficiency

    def is_active(self):
        return self.active

    def shuffle_question_vector(self):
        return random.sample(self.questions, len(self.questions))

    def get_topic_id(self):
        return self.topic_id

    def contains_question(self, q):
        return any(que.get_question() == q for que in self.questions)