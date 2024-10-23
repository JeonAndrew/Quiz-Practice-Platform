#ifndef QUESTION_H
#define QUESTION_H

#include <string>
#include <vector>

class Question {
public:
    Question();
    Question(std::string t);
    //todo

private:
    //usage:
    //get index of your question
    //use matching index for correct answer
    //use matching index to ACCESS a vector of possible incorrect answers; pick any amount of them
    //dont need to use incorrectAnswers_ if it's a short response question
    std::vector<std::string> questions_;
    std::vector<std::string> correctAnswers_;
    std::vector<std::vector<std::string>> incorrectAnswers_;
    std::string topic_;
};

#endif // QUESTION_H