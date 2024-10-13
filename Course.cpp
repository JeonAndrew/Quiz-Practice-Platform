#include "Course.h"

// constructor
Course::Course(const std::string& name) {
    courseName_ = name;
}

// adds topic to course
void Course::addTopic(const std::string& topic) {
    topics_.push_back(topic);
}

// removes topic from course
// if you try to remove a topic that doesn't exist, it will do nothing
// for now have added an std::cout statement for the above case
void Course::removeTopic(const std::string& topic) {
    auto it = std::find(topics_.begin(), topics_.end(), topic);
    if (it != topics_.end()) {
        topics_.erase(it);
        return;
    }
    std::cout << "please remove a topic that exists in the courselist" << std::endl;
    return; // topic not found
}

// returns the index of a given topic. can find topic names thru listTopics()
// probably not for user use
int Course::findTopic(const std::string& topic) const {
    auto it = std::find(topics_.begin(), topics_.end(), topic);
    if (it != topics_.end()) {
        return std::distance(topics_.begin(), it);
    }
    return -1; // topic not found
}

// precondition: topics_ is not empty
// probably not for user use
void Course::listTopics() const {
    std::cout << "Topics currently in " << courseName_ << ": ";
    for (const auto& topic : topics_) {
        if (topic == topics_.at(0)) {
            std::cout << topic << std::endl;
        } else {
            std::cout << ", " << topic << std::endl;
        }
    }
}
