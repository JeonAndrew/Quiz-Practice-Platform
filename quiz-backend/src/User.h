#include "quiz.h"
#include <list>
#include <vector>
#include <map>
#include <string>

class User {
    public:
        User();
        void resetStreak();
        int getStreak();
        void addToStreak();
        std::list<double> getPerformance();
        void setLatestPerformance();
        Quiz getQuiz();
        void setQuiz(Quiz quiz);
        std::map<std::string, int> getProficiencies();

    private:
        std::list<double> performance_;
        int streak_ = 0;
        Quiz recentQuiz_;
        std::map<std::string, int> proficiencies_;
};