import unittest
from unittest.mock import MagicMock
from quiz import Quiz  

class MockTopic:
    def __init__(self, name, active=True, proficiency=5):
        self.name = name
        self.active = active
        self.proficiency = proficiency

    def is_active(self):
        return self.active

    def get_proficiency(self):
        return self.proficiency

    def shuffle_question_vector(self):
        """Simulate a shuffled list of questions."""
        return [MockQuestion(correct=True) for _ in range(15)]

    def increment(self):
        pass

    def decrement(self):
        pass


class MockQuestion:
    def __init__(self, correct):
        self.correct = correct

    def is_correct(self, user_answer):
        return user_answer


class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.topics = [
            MockTopic(name="Topic 1", active=True, proficiency=5),
            MockTopic(name="Topic 2", active=True, proficiency=10),
            MockTopic(name="Topic 3", active=False, proficiency=5),  # Inactive topic
        ]
        self.quiz = Quiz(self.topics)

    def test_initialization(self):
        self.assertEqual(len(self.quiz.get_questions()), 30)
        self.assertEqual(len(self.quiz.question_topics), 30)
        self.assertFalse(self.quiz.has_submitted())
        self.assertIsNone(self.quiz.get_result())

    def test_questions_selected_from_active_topics(self):
        for topic in self.quiz.question_topics:
            self.assertTrue(topic.is_active())

    def test_submission_all_correct(self):
        user_answers = [True] * Quiz.kNumQuestions  # All answers are correct
        self.quiz.submission(user_answers)

        self.assertTrue(self.quiz.has_submitted())
        self.assertEqual(self.quiz.get_result(), 1.0)  # 100% correct
        self.assertTrue(all(self.quiz.question_correct))

    def test_submission_all_incorrect(self):
        user_answers = [False] * Quiz.kNumQuestions  # All answers are incorrect
        self.quiz.submission(user_answers)

        self.assertTrue(self.quiz.has_submitted())
        self.assertEqual(self.quiz.get_result(), 0.0) 
        self.assertFalse(any(self.quiz.question_correct))

    def test_submission_mixed_results(self):
        user_answers = [i % 2 == 0 for i in range(Quiz.kNumQuestions)] 
        self.quiz.submission(user_answers)

        expected_score = sum(1 for i in range(Quiz.kNumQuestions) if i % 2 == 0) / Quiz.kNumQuestions
        self.assertTrue(self.quiz.has_submitted())
        self.assertAlmostEqual(self.quiz.get_result(), expected_score)
        self.assertEqual(self.quiz.question_correct.count(True), (Quiz.kNumQuestions // 2) + 1)


if __name__ == "__main__":
    unittest.main()
