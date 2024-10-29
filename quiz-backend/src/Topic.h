#ifndef TOPIC_H
#define TOPIC_H

#include <vector>
#include "Question.h"  // todo

class Topic {
public:
    Topic(std::string name, int proficiency);
    std::string getName();
    void increment();
    void decrement();
    void activate();
    void deactivate();
    void addQuestion(const Question& question);
    int getProficiency();
    bool isActive();
    Question getRandomQuestion();

private:
    std::string topicName_;
    int proficiency_;
    std::vector<Question> questions_;
    bool active_ = true;
};

#endif
