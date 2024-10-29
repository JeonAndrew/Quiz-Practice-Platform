#include "Course.h"
//test
// constructor
Course::Course(const std::string& name, const int& cID) : name_(name), courseID_(cID) {}

// adds topic to course
void Course::addTopic(Topic& t) {
    topics_.push_back(t);
}

// removes topic from course
// if you try to remove a topic that doesn't exist, it will do nothing
// for now have added an std::cout statement for the above case
void Course::removeTopic(const int& tID) {
    for (auto it = topics_.begin(); it != topics_.end(); it++) {
        if (it->getTopicID() == tID) {
            topics_.erase(it);
            return;
        }
    }
    std::cout << "please remove a topic that exists in the courselist" << std::endl;
    return; // topic not found
}

// returns the index of a given topic. can find topic names thru listTopics()
// probably not for user use
int Course::findTopic(const int& tID) const {
    for (auto it = topics_.begin(); it != topics_.end(); it++) {
        if (it->getTopicID() == tID) {
            return std::distance(topics_.begin(), it);
        }
    }
    return -1; // topic not found
}

// precondition: topics_ is not empty
// probably not for user use
void Course::listTopics() const {
    std::cout << "Topics currently in " << courseName_ << ": ";
    for (unsigned int i = 0; i < topics_.size() - 1; i++) {
        std::cout << topics_[i].getName() << std::endl;
        std::cout << ", " << std::endl;
    }
    std::cout << topics_[topics.size() - 1].getName() << std::endl;
}

std::vector<Topic> Course::getTopics() {
    return topics_;
}

int Course::getCourseID() const {
    return courseID_;
}