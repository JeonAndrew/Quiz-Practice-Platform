#include "Question.h"
#include <iostream>

// constructor
Question::Question() {}

Question::Question(std::string t) {
    topic_ = t;
}

//todo
void Question::addQuestion(int index, std::string q, std::string ans, std::vector<std::string> wrongs) {
    questions_.at(index) = q;
    correctAnswers_.at(index) = ans;
    incorrectAnswers.at(index) = wrongs;
    return;
}