import unittest
from course import Course 

class MockTopic:
    def __init__(self, topic_id, name):
        self.topic_id = topic_id
        self.name = name

    def get_topic_id(self):
        return self.topic_id

    def get_name(self):
        return self.name


class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course = Course("Math 101", 1)
        self.topic1 = MockTopic(101, "Algebra")
        self.topic2 = MockTopic(102, "Calculus")
        self.topic3 = MockTopic(103, "Geometry")

    def test_initialization(self):
        self.assertEqual(self.course.course_name, "Math 101")
        self.assertEqual(self.course.get_course_id(), 1)
        self.assertEqual(self.course.get_topics(), [])

    def test_add_topic(self):
        self.course.add_topic(self.topic1)
        self.assertIn(self.topic1, self.course.get_topics())
        self.assertEqual(len(self.course.get_topics()), 1)

        self.course.add_topic(self.topic2)
        self.assertIn(self.topic2, self.course.get_topics())
        self.assertEqual(len(self.course.get_topics()), 2)

    def test_find_topic(self):
        self.course.add_topic(self.topic1)
        self.course.add_topic(self.topic2)

        self.assertEqual(self.course.find_topic(101), 0)
        self.assertEqual(self.course.find_topic(102), 1)

        self.assertEqual(self.course.find_topic(999), -1)

    def test_find_topic_edge_case(self):
        self.assertEqual(self.course.find_topic(101), -1)

    def test_list_topics(self):
        self.course.add_topic(self.topic1)
        self.course.add_topic(self.topic2)

        # have to ensure correct printing here using io and sys
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        self.course.list_topics()

        sys.stdout = sys.__stdout__  
        output = captured_output.getvalue()

        self.assertIn("Topics currently in Math 101:", output)
        self.assertIn("- Algebra", output)
        self.assertIn("- Calculus", output)

    def test_get_topics(self):
        self.assertEqual(self.course.get_topics(), [])

        self.course.add_topic(self.topic1)
        self.assertEqual(self.course.get_topics(), [self.topic1])

        self.course.add_topic(self.topic2)
        self.assertEqual(self.course.get_topics(), [self.topic1, self.topic2])


if __name__ == "__main__":
    unittest.main()
