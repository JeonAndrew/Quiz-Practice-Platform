#include <vector>
#include <map>
#include "Question.h"

class Quiz {
    public:
        Quiz();
        void setResult(double score);
        double getResult();
        void generateQuestions(std::map<std::string, int> profs);
        std::vector<Question> getQuestions();

    private:
        double result_;
        std::vector<Question> questions_;
};