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

    def to_dict(self):
        return {
            'question': self.question,
            'options': self.options,
            'correct_answer': self.correct_answer,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            question=data.get('question'),
            options=data.get('options', []),
            correct_answer=data.get('correct_answer'),
        )
    

    