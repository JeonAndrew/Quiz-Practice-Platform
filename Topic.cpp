#include "Topic.h"

// Constructor
Topic::Topic() : proficiency_(0) {}

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
