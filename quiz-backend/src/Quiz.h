#pragma once

#include <vector>
#include <map>
#include "Question.h"
#include "User.h"
#include "Topic.h"

class Quiz {
    public:
        Quiz(std::vector<Topic>& topics);
        double getResult() const ;
        std::vector<Question> getQuestions() const;
        void submission(std::vector<std::string>& answers);
        bool hasSubmitted() const;

    private:
        const int kNumQuestions = 15;
        const int kMaxProficiency = 20;
        double result_;
        std::vector<Question> questions_;
        std::vector<bool> questionCorrect(kNumQuestions);
        bool submissionStatus = false;
};