import random

class Quiz:
    kNumQuestions = 15
    kMaxProficiency = 20

    def __init__(self, topics):
        self.result = None
        self.questions = []
        self.question_topics = []
        self.question_correct = [False] * self.kNumQuestions
        self.submission_status = False

        # First step is to sum all of the proficiency scores for active topics
        total_proficiency = sum(t.get_proficiency() for t in topics if t.is_active())

        # Passing each percentage interval into a vector with the topic name linked to the percentage
        # If there were 5 topics with the same proficiency, we would have a vector of: [0.20, 0.40, 0.60, 0.80, 1.00]
        percents = []
        next_val = 0.0

        # Percents array will be made up of keys and values that contain the topic,
        # list of randomized questions, and the odds of that topic
        for t in topics:
            if t.is_active():
                topic_data = {}
                topic_data["topic"] = t
                topic_data["questions"] = t.shuffle_question_vector()
                proficiency_factor = (self.kMaxProficiency - t.get_proficiency()) / total_proficiency
                topic_data["odds"] = next_val + proficiency_factor
                percents.append(topic_data)
                next_val += proficiency_factor

        # Generating a random number and seeing where it lies on the percentage vector to 
        # see what type of topic this question is and then taking a random question from that topic
        for i in range(self.kNumQuestions):
            random_percent = random.random()
            for topic_data in percents:
                if random_percent <= topic_data["odds"]:
                # Using the randomly generated vector of questions to access a random question without duplicates
                    self.questions.append(topic_data["questions"][i])
                    self.question_topics.append(topic_data["topic"])

    def get_result(self):
        return self.result

    def get_questions(self):
        return self.questions

    def has_submitted(self):
        return self.submission_status

    def submission(self, user_answers):
        # Keep count to eventually calculate score
        count_correct = 0

        # Go through each question in the Quiz and check to see if the submitted answer is correct
        # If yes, incrememnt proficiency and mark Question as True, decrememnt and mark False otherwise
        for i in range(self.kNumQuestions):
            if questions[i].is_correct(user_answers[i]):
                self.question_correct[i] = True
                count_correct += 1
                self.question_topics[i].increment()  
            else:
                self.question_topics[i].decrement()  

        # Calculate result as percentage of correct answers
        self.result = count_correct / self.kNumQuestions
        self.submission_status = True
