#ifndef QUESTION_H
#define QUESTION_H

#include <string>
#include <vector>

class Question {
public:
    Question();
    Question(std::string q, std::vector<std::string> options, std::string answer);
    bool isCorrect(std::string submission);
    std::vector<std::string> getOptions();
    std::string getQuestion();
    std::string getCorrectAnswer();

private:
    std::string question_;
    std::string correctAnswer_;
    std::vector<std::string> options_;
};

#endif // QUESTION_H
