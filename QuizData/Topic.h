#ifndef TOPIC_H
#define TOPIC_H

#include <vector>
#include "Question.h"  // todo

class Topic {
public:
    Topic();
    void increment();
    void decrement();

private:
    int proficiency_;
    std::vector<Question> questions_;
};

#endif
