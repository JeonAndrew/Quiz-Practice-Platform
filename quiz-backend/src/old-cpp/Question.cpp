#include "Question.h"
#include <iostream>

// constructor
Question::Question() {}

// Creates a question after being provided with the question, options, and answer
Question::Question(std::string q, std::vector<std::string> options, std::string answer) {
    question_ = q;
    options_ = options;
    answer_ = answer;
}

// Returns whether the user's submission for the current question is correct
bool Question::isCorrect(std::string submission) {
    return submission == answer_;
}

std::vector<std::string> Question::getOptions() {
    return options_;
}

std::string Question::getQuestion() {
    return question_;
}

std::string Question::getCorrectAnswer() {
    return correctAnswer_;
}
