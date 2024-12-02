#include "Topic.h"

// Constructor that instantiates the proficiency for a user as well as the name of the topic
// The proficiency will be gathered from the DB
Topic::Topic(std::string name, int tID, int proficiency) : proficiency_(proficiency), topicID_(tID) topicName_(name) {}


std::string Topic::getName() const {
    return name_;
}

// Increment proficiency
void Topic::increment() {
    if (proficiency_ < kMaxProficiency) { //can decide on number later
        ++proficiency_;
    }
}

// Decrement proficiency
void Topic::decrement() {
    if (proficiency_ > 0) {
        --proficiency_;
    }
}

void Topic::activate() {
    active_ = true;
}

void Topic::deactivate() {
    active_ = false;
}

void Topic::addQuestion(const Question& question) {
        questions_.push_back(question);
    }

int Topic::getProficiency() const {
    return proficiency_;
}

bool Topic::isActive() const {
    return active_;
}

Question Topic::getRandomQuestion() const {
    std::srand(static_cast<unsigned int>(time(0)));
    int randIndex = std::rand() % questions_.size();
    return questions_[randIndex];
}

std::vector<Question> Topic::shuffleQuestionVector() {
    std::vector<Question> shuffledQuestions(questions_);
    std::random_shuffle(shuffledQuestions.begin(), shuffledQuestions.end());
    return shuffledQuestions;
}

int Topic::getTopicID() const {
    return topicID_;
}

bool Topic::containsQuestion(std::string q) {
    for (Question que : questions_) {
        if (que.getQuestion() == q) {
            return true;
        }
    }
    return false;
}