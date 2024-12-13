from models.Question import Question

class Quiz:
    kQuestionsPerTopic = 5  # Number of questions per topic

    def __init__(self, topics):
        self.result = None
        self.questions = []
        self.question_topics = []
        self.question_correct = []
        self.submission_status = False

        for topic in topics:
            if topic.is_active():
                shuffled_questions = topic.shuffle_question_vector()
                selected_questions = shuffled_questions[:self.kQuestionsPerTopic]
                self.questions.extend(selected_questions)
                self.question_topics.extend([topic] * len(selected_questions))

        self.question_correct = [False] * len(self.questions)

    def to_dict(self):
        return {
            'result': self.result,
            'questions': [q.to_dict() for q in self.questions],
            'question_topics': [t.get_topic_id() for t in self.question_topics],
            'question_correct': self.question_correct,
            'submission_status': self.submission_status,
        }

    @classmethod
    def from_dict(cls, data, topics):
        quiz = cls(topics=[])  # We'll set attributes manually
        quiz.result = data.get('result')
        quiz.questions = [Question.from_dict(q_data) for q_data in data.get('questions', [])]
        quiz.question_topics = []
        for topic_id in data.get('question_topics', []):
            topic = next((t for t in topics if t.get_topic_id() == int(topic_id)), None)
            if topic:
                quiz.question_topics.append(topic)
        quiz.question_correct = data.get('question_correct', [])
        quiz.submission_status = data.get('submission_status', False)
        return quiz

    def get_result(self):
        return self.result

    def get_questions(self):
        return self.questions

    def has_submitted(self):
        return self.submission_status

    def submission(self, user_answers):
        count_correct = 0

        # user_answers is a list of answers for each question
        for i in range(len(self.questions)):
            if self.questions[i].is_correct(user_answers[i]):
                self.question_correct[i] = True
                count_correct += 1
                self.question_topics[i].increment()
            else:
                self.question_topics[i].decrement()

        self.result = count_correct / len(self.questions)
        self.submission_status = True

        