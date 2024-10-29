#include "Topic.h"

// Constructor that instantiates the proficiency for a user as well as the name of the topic
// The proficiency will be gathered from the DB
Topic::Topic(std::string name, int proficiency) : proficiency_(proficiency), topicName_(name) {}


std::string Topic::getName() {
    return name_;
}

// Increment proficiency
void Topic::increment() {
    if (proficiency_ < 20) { //can decide on number later
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

int Topic::getProficiency() {
    return proficiency_;
}

bool Topic::isActive() {
    return active_;
}

Question Topic::getRandomQuestion() {
    std::srand(static_cast<unsigned int>(time(0)));
    int randIndex = std::rand() % questions_.size();
    return questions_[randIndex];
}