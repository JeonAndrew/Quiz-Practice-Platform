import unittest
from topic import Topic 

class MockQuestion:
    def __init__(self, question_text):
        self.question_text = question_text

    def get_question(self):
        return self.question_text


class TestTopic(unittest.TestCase):
    def setUp(self):
        self.topic = Topic("Math", 1, 10)
        self.mock_questions = [
            MockQuestion(f"Question {i}") for i in range(5)
        ]

    def test_initialization(self):
        self.assertEqual(self.topic.get_name(), "Math")
        self.assertEqual(self.topic.get_topic_id(), 1)
        self.assertEqual(self.topic.get_proficiency(), 10)
        self.assertTrue(self.topic.is_active())
        self.assertEqual(len(self.topic.questions), 0)

    def test_increment_proficiency(self):
        self.topic.increment()
        self.assertEqual(self.topic.get_proficiency(), 11)

        # Test maximum proficiency cap
        self.topic.proficiency = self.topic.kMaxProficiency
        self.topic.increment()
        self.assertEqual(self.topic.get_proficiency(), self.topic.kMaxProficiency)

    def test_decrement_proficiency(self):
        self.topic.decrement()
        self.assertEqual(self.topic.get_proficiency(), 9)

        # Test minimum proficiency cap
        self.topic.proficiency = 0
        self.topic.decrement()
        self.assertEqual(self.topic.get_proficiency(), 0)

    def test_activate_deactivate(self):
        self.topic.deactivate()
        self.assertFalse(self.topic.is_active())

        self.topic.activate()
        self.assertTrue(self.topic.is_active())

    def test_add_question(self):
        self.topic.add_question(self.mock_questions[0])
        self.assertEqual(len(self.topic.questions), 1)
        self.assertEqual(self.topic.questions[0].get_question(), "Question 0")

    def test_shuffle_question_vector(self):
        for q in self.mock_questions:
            self.topic.add_question(q)

        shuffled_questions = self.topic.shuffle_question_vector()
        self.assertCountEqual(shuffled_questions, self.topic.questions)
        self.assertNotEqual(shuffled_questions, self.topic.questions)  # Likely shuffled

    def test_contains_question(self):
        self.topic.add_question(self.mock_questions[0])

        self.assertTrue(self.topic.contains_question("Question 0"))
        self.assertFalse(self.topic.contains_question("Question 1"))


if __name__ == "__main__":
    unittest.main()
