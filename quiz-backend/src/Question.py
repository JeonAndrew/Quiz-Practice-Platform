class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.options = options

    def is_correct(self, submission):
        return submission == self.correct_answer

    def get_options(self):
        return self.options

    def get_question(self):
        return self.question

    def get_correct_answer(self):
        return self.correct_answer
