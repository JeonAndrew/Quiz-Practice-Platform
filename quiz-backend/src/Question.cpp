#include "Question.h"
#include <iostream>

// constructor
Question::Question() {}

// Creates a question after being provided with the question, options, and answer
Question::Question(std::string q, std::vector<string> options, std::string answer) {
    question_ = q;
    options_ = options;
    answer_ = answer;
}

// Returns whether the user's submission for the current question is correct
bool Question::isCorrect(std::string submission) {
    return submission == answer_;
}