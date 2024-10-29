#ifndef TOPIC_H
#define TOPIC_H

#include <vector>
#include "Question.h"  // todo

class Topic {
public:
    Topic(std::string name, int tID, int proficiency);
    std::string getName() const;
    void increment();
    void decrement();
    void activate();
    void deactivate();
    void addQuestion(const Question& question);
    int getProficiency() const;
    bool isActive() const;
    Question getRandomQuestion() const;
    int getTopicID() const;

private:
    std::string topicName_;
    int proficiency_;
    std::vector<Question> questions_;
    bool active_ = true;
    int topicID_;
};

#endif