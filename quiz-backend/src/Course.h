#ifndef COURSE_H
#define COURSE_H

#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include "Topic.h"
#include "Question.h"

class Course {
public:
    Course(const std::string& name, const int& cID);

    // Public member functions
    void addTopic(Topic& t);
    void removeTopic(const int& tID);
    int findTopic(const int& tID) const;
    void listTopics() const;
    std::vector<Topic> getTopics();
    int getCourseID() const;

private:
    std::vector<Topic> topics_;
    std::string courseName_;
    int courseID_;
};

#endif