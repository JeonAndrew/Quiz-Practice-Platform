import unittest
from question import Question 

class TestQuestion(unittest.TestCase):
    def setUp(self):
        self.question_text = "What is 2 + 2?"
        self.options = ["1", "2", "3", "4"]
        self.correct_answer = "4"
        self.question = Question(self.question_text, self.options, self.correct_answer)

    def test_initialization(self):
        self.assertEqual(self.question.get_question(), self.question_text)
        self.assertEqual(self.question.get_options(), self.options)
        self.assertEqual(self.question.get_correct_answer(), self.correct_answer)

    def test_is_correct(self):
        self.assertTrue(self.question.is_correct("4")) 
        self.assertFalse(self.question.is_correct("3"))  
        self.assertFalse(self.question.is_correct("1"))  
        self.assertFalse(self.question.is_correct("5"))  

    def test_get_question(self):
        self.assertEqual(self.question.get_question(), "What is 2 + 2?")

    def test_get_options(self):
        self.assertListEqual(self.question.get_options(), ["1", "2", "3", "4"])

    def test_get_correct_answer(self):
        self.assertEqual(self.question.get_correct_answer(), "4")


if __name__ == "__main__":
    unittest.main()
