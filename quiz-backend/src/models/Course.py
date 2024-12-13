class Course:
    def __init__(self, name, c_id):
        self.course_name = name
        self.course_id = c_id
        self.topics = []

    def add_topic(self, topic):
        self.topics.append(topic)

    def find_topic(self, t_id):
        for index, topic in enumerate(self.topics):
            if topic.get_topic_id() == t_id:
                return index
        return -1  

    def list_topics(self):
        print(f"Topics currently in {self.course_name}:")
        for topic in self.topics:
            print(f"- {topic.get_name()}")

    def get_topics(self):
        return self.topics

    def get_course_id(self):
        return self.course_id
    

    