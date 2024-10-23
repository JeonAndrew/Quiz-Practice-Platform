#ifndef TOPIC_H
#define TOPIC_H

#include <vector>
#include "Question.h"  // todo

class Topic {
public:
    Topic();
    std::string getName();
    std::string setName(std::string s);
    void increment();
    void decrement();
    void Topic::activate()
    void Topic::deactivate();
    void addQuestion(Question q);

private:
    std::string name_;
    int proficiency_;
    int userProficiency_;
    std::vector<Question> questions_;
};

#endif
