#include "Quiz.h"
#include <list>
#include <vector>
#include <map>
#include <string>

class User {
    public:
        User(int uid, int s);
        void resetStreak();
        int getStreak();
        void addToStreak();
        std::list<double> getPerformance();
        void setLatestPerformance();
        Quiz getQuiz();
        void setQuiz(Quiz quiz);
        int getUserID();

    private:
        int userID_;
        std::list<double> performance_;
        int streak_ = 0;
        Quiz recentQuiz_;
};
