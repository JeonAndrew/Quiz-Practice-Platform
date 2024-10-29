#pragma once

#include <vector>
#include <map>
#include "Question.h"

class Quiz {
    public:
        Quiz(std::vector<Topic>& topics);
        double getResult();
        std::vector<Question> getQuestions();
        void Quiz::submission(std::vector<std::string>& answers);

    private:
        double result_;
        std::vector<Question> questions_;
};