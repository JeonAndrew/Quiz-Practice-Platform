import unittest
from user import User 
from collections import deque

class MockQuiz:
    def __init__(self, result):
        self.result = result

    def get_result(self):
        return self.result

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(uid=1) 

    def test_user_id(self):
        self.assertEqual(self.user.get_user_id(), 1)

    def test_initial_performance(self):
        self.assertEqual(self.user.get_performance(), [])

    def test_streak_initial_value(self):
        self.assertEqual(self.user.get_streak(), 0)

    def test_add_to_streak(self):
        self.user.add_to_streak()
        self.assertEqual(self.user.get_streak(), 1)

        self.user.add_to_streak()
        self.assertEqual(self.user.get_streak(), 2)

    def test_reset_streak(self):
        self.user.add_to_streak()
        self.user.add_to_streak()
        self.assertEqual(self.user.get_streak(), 2)

        self.user.reset_streak()
        self.assertEqual(self.user.get_streak(), 0)

    def test_set_quiz_and_performance(self):
        quiz1 = MockQuiz(85)
        quiz2 = MockQuiz(90)

        self.user.set_quiz(quiz1)
        self.assertEqual(self.user.get_quiz(), quiz1)
        self.assertEqual(self.user.get_performance(), [85])

        self.user.set_quiz(quiz2)
        self.assertEqual(self.user.get_quiz(), quiz2)
        self.assertEqual(self.user.get_performance(), [85, 90])

    def test_performance_max_length(self):
        for i in range(1, 10):  # Add 9 quiz results
            quiz = MockQuiz(result=i * 10)
            self.user.set_quiz(quiz)

        # Only the last 7 results should remain
        expected_performance = [30, 40, 50, 60, 70, 80, 90]
        self.assertEqual(self.user.get_performance(), expected_performance)

    def test_recent_quiz_update(self):
        quiz1 = MockQuiz(75)
        quiz2 = MockQuiz(88)

        self.user.set_quiz(quiz1)
        self.assertEqual(self.user.get_quiz().get_result(), 75)

        self.user.set_quiz(quiz2)
        self.assertEqual(self.user.get_quiz().get_result(), 88)

if __name__ == '__main__':
    unittest.main()
