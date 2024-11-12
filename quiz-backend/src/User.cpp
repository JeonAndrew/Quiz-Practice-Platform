#include "User.h"

User::User(int uid) : userID_(uid) {}

// Will execute when user misses a day, resetting the streak to 0
void User::resetStreak() {
    streak_ = 0;
}

int User::getStreak() {
    return streak_;
}

// Adds one day to the streak
void User::addToStreak() {
    streak_++;
}

// Returns the performance of the last 7 quizzes
std::list<double> User::getPerformance() {
    return performance_;
}

// If the user has less than 7 quizzes completed, add a result to the end of the list
// If the user has 7 quizzes completed, erase the data of the oldest quiz, replacing with the newest quiz at the end
void User::setLatestPerformance() {
    if (performance_.size() < 7) {
        performance_.push_back(recentQuiz_.getResult());
    } else {
        performance_.pop_front();
        performance_.push_back(recentQuiz_.getResult());
    }
}

// Returns the last quiz the user compelted
Quiz User::getQuiz() {
    return recentQuiz_;
}

// Sets the latest quiz that a user completed and adds it to the performance vector
void User::setQuiz(Quiz quiz) {
    recentQuiz_ = quiz;
    setLatestPerformance();
}

int User::getUserID() {
    return userID_;
}