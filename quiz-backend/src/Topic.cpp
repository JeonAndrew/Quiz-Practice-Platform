#include "Topic.h"

// Constructor
Topic::Topic() : proficiency_(10) {}


std::string Topic::getName() {
    return name_;
}

std::string Topic::setName(std::string in) {
    name_ = in;
    return std::string();
}

// Increment proficiency
void Topic::increment() {
    if (proficiency_ < 20) { //can decide on number later
        ++userProficiency_;
    }
    proficiency_ = userProficiency_;
    return;
}

// Decrement proficiency
void Topic::decrement() {
    if (proficiency_ > 0) {
        --userProficiency_;
    }
    proficiency_ = userProficiency_;
    return;
}

void Topic::activate() {
    proficiency_ = userProficiency_;
}

void Topic::deactivate() {
    proficiency_ = -1;
}

void Topic::addQuestion(Question q) {
    questions_.push_back(q);
}