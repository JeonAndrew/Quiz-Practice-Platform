#ifndef COURSE_H
#define COURSE_H

#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

class Course {
public:
    Course(const std::string& name);

    // Public member functions
    void addTopic(const std::string& topic);
    void removeTopic(const std::string& topic);
    int findTopic(const std::string& topic) const;
    void listTopics() const;

private:
    std::vector<std::string> topics_;
    std::string courseName_;
};

#endif
