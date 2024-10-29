#pragma once

#include <vector>
#include <map>
#include "Question.h"

class Quiz {
    public:
        Quiz(std::vector<Topic>& topics);
        double getResult() const ;
        std::vector<Question> getQuestions() const;
        void submission(std::vector<std::string>& answers);
        bool hasSubmitted() const;

    private:
        double result_;
        std::vector<Question> questions_;
        std::vector<bool> questionCorrect(15);
        bool submissionStatus = false;
};